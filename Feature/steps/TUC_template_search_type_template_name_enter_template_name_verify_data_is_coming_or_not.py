import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter template name')
def step_impl(context):
    context.driver.find_element(By.ID, "search-id").send_keys("English Short")


@then(u'Verify data present or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[1]/th[2]").text
    if txt == "Template Name":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"
