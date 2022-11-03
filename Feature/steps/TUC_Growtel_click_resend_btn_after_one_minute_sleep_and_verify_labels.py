import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on resend otp')
def step_impl(context):
    time.sleep(2)
    resend_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/a")
    context.driver.execute_script("arguments[0].click();", resend_button)


@then(u'verify after 1 minute')
def step_impl(context):
    time.sleep(65)
    resend_button = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/a")
    context.driver.execute_script("arguments[0].click();", resend_button)
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/p").text
    if txt == "The OTP has been sent to your Email ID ":
        assert True, f"{txt}"
    elif txt == "ronit*****@onextel.tech":
        assert True, f"{txt}"
    elif txt == " and your Phone Number ":
        assert True, f"{txt}"
    elif txt == "7008****74":
        assert True, f"{txt}"
    elif txt == "The OTP has been sent to your Email ID ronit*****@onextel.tech and your Phone Number 7008****74":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
