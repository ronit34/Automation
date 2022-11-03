import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'verify resend button error label')
def step_impl(context):
    time.sleep(2)
    resend_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/a")
    context.driver.execute_script("arguments[0].click();", resend_button)

    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/p").text
    if txt == "OTP already sent...wait for 58 seconds for the next retry":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"