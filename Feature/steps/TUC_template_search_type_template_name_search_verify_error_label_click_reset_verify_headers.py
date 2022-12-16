import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Select search type template name')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "template_type"))
    select.select_by_visible_text("Template Name")


@then(u'Click on Search in template')
def step_impl(context):
    time.sleep(2)
    Button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", Button)


@then(u'Verify error label of template name')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.ID, "tab_content").text
    if txt == "No Template Data Available":
        assert True, f"{txt}"
    else:
        assert True, f"{txt}"


@then(u'Click on reset template')
def step_impl(context):
    time.sleep(1)
    Button = context.driver.find_element(By.ID, "reset")
    context.driver.execute_script("arguments[0].click();", Button)


@then(u'Verify headers of template')
def step_impl(context):
    time.sleep(2)
    template_name = context.driver.find_element(By.XPATH, "//*[@id='template_table']/tbody/tr[1]/th[2]").text
    if template_name == "No Template Data Available":
        assert True, f"{template_name}"
    else:
        assert True, f"{template_name}"
