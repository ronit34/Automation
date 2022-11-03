from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Check for error message in add campaign pop up')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[1]/span/span").text
    if text == "Campaign Name Already exists":
        assert True, "Campaign Name Already exists"
    else:
        assert False, "Campaign Name does not exists"

