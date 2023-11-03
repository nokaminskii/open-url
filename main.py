from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_user_login():
    user_name = "minskw434i@gmail.com"
    password = "dsewerer"
    browser_url ="https://portal.ustraveldocs.com/"

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    time.sleep(5)
    driver.get(browser_url)
    driver.maximize_window()
    driver.find_element(By.ID, "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username").send_keys(user_name)
    driver.implicitly_wait(15)
    time.sleep(5)
    driver.find_element(By.ID, "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password").send_keys(password)
    driver.implicitly_wait(15)
    time.sleep(5)
    driver.find_element(By.NAME, "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167").click()
    driver.implicitly_wait(15)
    time.sleep(5)
    driver.find_element(By.ID, "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton").click()
    driver.implicitly_wait(15)
    time.sleep(10)
    error_message = driver.find_element(By.ID, "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:error:j_id132:j_id133:0:j_id134:j_id135:j_id137").text
    assert (error_message == "Ошибка.Неудачная попытка входа. Введите правильное имя пользователя и пароль.")


if __name__ == "__main__":
    test_user_login()
