from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


class AppPage:
    # Login locators
    START_SESSION_BUTTON = (By.LINK_TEXT, "Iniciar sessão")
    COOKIES_ACCEPT_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "kc-login")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".kc-feedback-text")
    # Logged in indicator
    LOGGED_IN_INDICATOR = (By.ID, "aLogout")

    # Vehicles
    VEHICLES_MENU = (By.CSS_SELECTOR, "a[href*='vehicles']")
    ADD_VEHICLE_BUTTON = (By.ID, "aNewVehicle")

    # Vehicle Form
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='comment']")
    PLATE_INPUT = (By.CSS_SELECTOR, "input[name='plate']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "select[name='type']")
    COUNTRY_OTHER_OPTION = (By.CSS_SELECTOR, "select[name='type'] option[value='0']")
    SAVE_VEHICLE_BUTTON = (By.CSS_SELECTOR, "a[type='submit']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "a[type='button']")
    # VEHICLE LIST
    VEHICLE_LIST_ITEMS = (By.CSS_SELECTOR, "div.span2.bg.vehicles")
    EDIT_IN_ROW = (By.CSS_SELECTOR, "a.vehiclebtnbig")
    REMOVE_VEHICLE_BUTTON = (By.CSS_SELECTOR, "a.close")
    CONFIRM_REMOVE_BUTTON = (By.CSS_SELECTOR, "#deleteConfirmModal .btn-success")

    # Initialization
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text


    # LOGIN
    def set_email(self, email):
        self._type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self._type(self.PASSWORD_INPUT, password)


    def click_login(self):
        self._click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self._click(self.START_SESSION_BUTTON)
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def get_login_error(self):
        return self._get_text(self.LOGIN_ERROR_MESSAGE)

    def is_logged_in(self):
        return self._find(self.LOGGED_IN_INDICATOR).is_displayed()

    # ADD VEHICLES
    def open_vehicles(self):
        try:
            self._click(self.COOKIES_ACCEPT_BUTTON)
        except Exception:
            pass
        menu = self.wait.until(EC.element_to_be_clickable(self.VEHICLES_MENU))
        menu.click()


    def click_new_vehicle(self):
        botao = self.wait.until(EC.presence_of_element_located(self.ADD_VEHICLE_BUTTON))
        self.driver.execute_script("arguments[0].click();", botao)


    def set_vehicle_name(self, name):
        self._type(self.NAME_INPUT, name)

    def select_country(self, country):
        Select(self._find(self.COUNTRY_SELECT)).select_by_visible_text(country)

    def set_plate(self, plate):
        self._type(self.PLATE_INPUT, plate)

    def click_save_vehicle(self):
        botao = self.wait.until(EC.presence_of_element_located(self.SAVE_VEHICLE_BUTTON))
        self.driver.execute_script("arguments[0].click();", botao)

    def add_vehicle(self, name, country, plate):
        self.click_new_vehicle()
        self.set_vehicle_name(name)
        self.select_country(country)
        self.set_plate(plate)
        self.click_save_vehicle()
        time.sleep(2)

    def get_vehicles(self):
        items = self.driver.find_elements(*self.VEHICLE_LIST_ITEMS)
        return [item.text.upper() for item in items]

   # REMOVE VEHICLE

    def remove_vehicle(self, plate):
        time.sleep(2)
        try:
            self._click(self.COOKIES_ACCEPT_BUTTON)
        except Exception:
            pass
        items = self.driver.find_elements(*self.VEHICLE_LIST_ITEMS)
        texts = [item.text.upper() for item in items]
        for index, text in enumerate(texts):
            if plate.upper() in text:
                items[index].find_element(*self.EDIT_IN_ROW).click()
                self._click(self.REMOVE_VEHICLE_BUTTON)
                time.sleep(1)
                self._click(self.CONFIRM_REMOVE_BUTTON)
                return
        raise ValueError(f"Vehicle with plate {plate} not found")











