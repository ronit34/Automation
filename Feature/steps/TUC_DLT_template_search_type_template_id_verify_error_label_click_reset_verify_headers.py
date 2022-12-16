import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Select search type template id')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "template_type"))
    select.select_by_visible_text("Template ID")


@then(u'Verify error label in template')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.ID, "tab_content").text
    if txt == "No Template Data Available":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"