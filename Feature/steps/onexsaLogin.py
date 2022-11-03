from behave import *
from selenium.webdriver.common.by import By
import time
@then(u'check iteratively login')
def step_impl(context):
    login(context, "onexsa", "onexsa")

def login(context, username, password):
    i=0
    while i<=5:
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver = driver

        context.driver.get("http://localhost:8000/index")
        context.driver.find_element(By.ID, "email").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)
        context.driver.implicitly_wait(100)

        # login button press
        button = context.driver.find_element(By.ID, "login_button")
        context.driver.execute_script("arguments[0].click();", button)
        print(f"login Number-----------------------------------> {i}")

        i=i+1

        time.sleep(1)
        context.driver.close()

