import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on CSV download')
def step_impl(context):
    time.sleep(2)
    Button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", Button)
    time.sleep(2)
    Button1 = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", Button1)
    time.sleep(2)
    Button2 = context.driver.find_element(By.ID, "Download")
    context.driver.execute_script("arguments[0].click();", Button2)
