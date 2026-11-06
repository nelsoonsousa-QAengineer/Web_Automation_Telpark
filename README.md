# Telpark Web Portal Automation

Automated tests built with Selenium and Pytest (Page Object Model) covering the Login and Vehicles functionalities of the web portal.

## ## Covered Tests

* Successful login
* Unsuccessful login (intentional)
* Add vehicle successfully selecting "Other" as country
* Remove vehicle successfully

## ## Structure

* **data.py**: test data (URL, credentials, license plate)
* **pages.py**: Page Object containing locators and actions
* **main.py**: test suite with asserts
* **requirements.txt**: project dependencies

## ## How to Run

1. Install Python 3 and Google Chrome.
2. Create and activate your virtual environment.
3. Install the dependencies: `pip install -r requirements.txt`
4. Fill in the data fields in `data.py` with a test account.
5. Execute: `pytest main.py -v`
