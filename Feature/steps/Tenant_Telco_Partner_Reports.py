from behave import *
import time

@then(u'click on download of partner summary')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("dropdownMenuLink").click()

    time.sleep(1)
    context.driver.find_element_by_id("download_csv").click()
    time.sleep(1)
    context.driver.find_element_by_id("Download").click()
