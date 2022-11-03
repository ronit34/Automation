import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Edit user')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[8]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter invalid mobile number and update')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "mob_no").clear()
    time.sleep(2)
    context.driver.find_element(By.ID, "mob_no").send_keys("12345")

    button = context.driver.find_element(By.ID, "update_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check invalid number is present or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/p").text

    if txt == "The OTP has been sent to your Email ID ronit*****@onextel.tech":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
