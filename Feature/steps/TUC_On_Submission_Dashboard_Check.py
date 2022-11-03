from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Check for Submitted Percent text in Pie Chart')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dlr_content']/div[1]/div/p[1]").text
    if text == "Submitted Percent":
        assert True, "'Submitted Percent' Text Present"
    else:
        assert False, "'Submitted Percent' Text Not Present"