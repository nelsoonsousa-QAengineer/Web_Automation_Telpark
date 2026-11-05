from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import data
from pages import AppPage

class TestApp:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        #cls.driver.maximize_window()

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(data.TELPARK_URL)
        self.page = AppPage(self.driver)

        try:
            accept_cookies = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_cookies.click()
        except Exception:
            pass

    def teardown_method(self):
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

    #LOGIN
    def test_login_success(self):
        self.page.login(data.EMAIL_ADDRESS, data.PASSWORD)
        assert self.page.is_logged_in()

    def test_login_error(self):
        self.page.login(data.WRONG_EMAIL, data.WRONG_PASSWORD)
        assert self.page.get_login_error() == data.EXPECTED_LOGIN_ERROR

    #VEHICLES
    def test_add_vehicle_other_country(self):
        self.page.login(data.EMAIL_ADDRESS, data.PASSWORD)
        self.page.open_vehicles()

        self.page.add_vehicle(name=data.VEHICLE_NAME, country="Outro", plate=data.VEHICLE_PLATE)
        lista_de_veiculos = self.page.get_vehicles()
        assert any(data.VEHICLE_PLATE.upper() in veiculo for veiculo in lista_de_veiculos), \
            f"A matricula {data.VEHICLE_PLATE} nao foi encontrada na lista de veiculos cadastrados."


    def test_remove_vehicle(self):
        self.page.login(data.EMAIL_ADDRESS, data.PASSWORD)
        self.page.open_vehicles()
        self.page.add_vehicle(name=data.VEHICLE_NAME, country="Outro", plate=data.VEHICLE_PLATE)
        self.page.remove_vehicle(data.VEHICLE_PLATE)
        lista_de_veiculos = self.page.get_vehicles()
        assert not any(data.VEHICLE_PLATE.upper() in veiculo for veiculo in lista_de_veiculos), \
            f"Falha: A matricula {data.VEHICLE_PLATE} nao foi removida com sucesso da lista"






