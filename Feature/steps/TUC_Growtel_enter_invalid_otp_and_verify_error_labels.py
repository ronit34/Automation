import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter invalid otp')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "first").send_keys("1")
    time.sleep(2)
    context.driver.find_element(By.ID, "second").send_keys("2")
    time.sleep(2)
    context.driver.find_element(By.ID, "third").send_keys("3")
    time.sleep(2)
    context.driver.find_element(By.ID, "fourth").send_keys("3")
    time.sleep(2)
    context.driver.find_element(By.ID, "fifth").send_keys("4")
    time.sleep(2)
    context.driver.find_element(By.ID, "sixth").send_keys("5")
    time.sleep(2)
    verify_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/a[2]")
    context.driver.execute_script("arguments[0].click();", verify_button)
    time.sleep(2)


@then(u'Verify error label')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/p").text
    if txt == "OTP entered is invalid":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
