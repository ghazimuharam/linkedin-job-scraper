from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login(driver, email, password):
    """login

    Parameters
    ----------
    driver : webdriver
        selenium web driver
    email : str
    password : str

    Returns
    -------

    """

    if not email or not password:
        print("Arguments not satisfied")
        raise SystemExit

    driver.get("https://www.linkedin.com/login")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))

    email_elem = driver.find_element_by_id("username")
    email_elem.send_keys(email)

    password_elem = driver.find_element_by_id("password")
    password_elem.send_keys(password)
    password_elem.submit()

    is_login(driver=driver)


def is_login(driver):
    """Get login state

    Parameters
    ----------
    driver : webdriver
        selenium web driver

    Returns
    -------
    Boolean
        True if profile-nav-item id presenece
    """
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "profile-nav-item")))
        return True
    except TimeoutException:
        return False
