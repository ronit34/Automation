import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Check all buttons of 2fa page')
def step_impl(context):
    time.sleep(2)
    cancel_button_tx = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/a[1]").text
    if cancel_button_tx == "Cancel":
        assert True, f"{cancel_button_tx}"
    else:
        assert False, f"{cancel_button_tx}"

    verify_button_tx = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/a[2]").text
    if verify_button_tx == "Verify":
        assert True, f"{verify_button_tx}"
    else:
        assert False, f"{verify_button_tx}"

    verify_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/a[2]")
    context.driver.execute_script("arguments[0].click();", verify_button)
    time.sleep(2)

    cancel_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/a[1]")
    context.driver.execute_script("arguments[0].click();", cancel_button)

    time.sleep(2)
    check_cancel = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/p[2]").text
    if check_cancel == "Sign In":
        assert True, f"{check_cancel}"
    else:
        assert False, f"{check_cancel}"
