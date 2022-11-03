from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Check for Delivered Percent text in Pie Chart')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dlr_content']/div[1]/div/p[1]").text
    if text == "Delivered Percent":
        assert True, "'Delivered Percent' Text Present"
    else:
        assert False, "'Delivered Percent' Text Not Present"