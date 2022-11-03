import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Edit tuc')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'uncheck 2fa and update')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div["
                                                   "1]/div[25]/div/div/div/label/input")
    context.driver.execute_script("arguments[0].click();", button)

    update_button = context.driver.find_element(By.ID, "update_tuc")
    context.driver.execute_script("arguments[0].click();", update_button)


@then(u'Verify login or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/p[1]").text
    if txt == "Dashboard":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
