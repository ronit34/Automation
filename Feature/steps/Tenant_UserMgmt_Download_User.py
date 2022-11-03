from behave import *
import time

@then(u'Click on download of pop up window')
def user(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("Download")
    context.driver.execute_script("arguments[0].click();", button)