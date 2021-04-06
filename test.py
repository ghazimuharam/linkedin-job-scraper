from selenium import webdriver
from src.Models.company import Company
from src import actions


""" Test Configuration

Initiate Chrome WebDriver
Test Login with Credentials
Test URL
"""

driver = webdriver.Chrome()
LINKEDIN_EMAIL = "yourlinkedinemail"
LINKEDIN_PASSWORD = "yourlinkedinpassword"

url = "https://www.linkedin.com/company/xiaomiindonesia/about/"


def test_login():

    actions.login(driver, LINKEDIN_EMAIL, LINKEDIN_PASSWORD)
    assert actions.is_login(driver=driver) == True, "Login Failed"


def test_get_company():
    company = Company(url=url, driver=driver)

    assert company.name == "Xiaomi Indonesia"
    assert company.industry == "Internet"
    assert company.company_size == "51-200 employees"
    assert company.headquarters == "Jakarta Utara, DKI Jakarta"
