import time
from behave import *

@then(u'enter data in search bar in tuc "{data}"')
def step_impl(context, data):
    context.driver.find_element_by_id("tuc_input").send_keys(data)