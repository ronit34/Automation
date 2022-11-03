import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter invalid email and number and update')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "email").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "email").send_keys("ronit")

    time.sleep(2)
    context.driver.find_element(By.ID, "mob_no").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "mob_no").send_keys("12345")

    button = context.driver.find_element(By.ID, "update_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check invalid email and number are present or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/p").text

    if txt == "Your email and phone number is invalid.Please contact support Team.":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"