from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Check for appeared Error Label')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='namepanel']/span").text
    if text == "already exists.":
        assert True, "TUC Already exists"
    else:
        assert False, "TUC does not exists"

