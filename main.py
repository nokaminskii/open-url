from selenium import webdriver
from selenium.webdriver.common.by import By


def test_user_login():
    user_name = "nokaminskii@gmail.com"
    password = "123456"
    browser_url ="https://magento.softwaretestingboard.com/customer/account/login"

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(browser_url)
    driver.maximize_window()
    driver.find_element(By.ID, "email").send_keys(user_name)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    driver.implicitly_wait(5)
    error_message = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert (error_message == "The account sign-in was incorrect or your account is disabled temporarily."
                             " Please wait and try again later.")



