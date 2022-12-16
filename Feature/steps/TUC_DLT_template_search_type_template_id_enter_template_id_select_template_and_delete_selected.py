import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Select a template and delete selected')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[4]/td[1]/label/input")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "delete_template")
    context.driver.execute_script("arguments[0].click();", button1)

    time.sleep(2)
    button2 = context.driver.find_element(By.ID, "delete")
    context.driver.execute_script("arguments[0].click();", button2)