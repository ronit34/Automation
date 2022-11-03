import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter invalid email and update')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "email").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "email").send_keys("ronit")

    button = context.driver.find_element(By.ID, "update_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check invalid email is present or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/p").text

    if txt == "The OTP has been sent to your Phone Number 7008****74":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"