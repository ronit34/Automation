from behave import *
import time

# @then(u'check text of Totals of partner summary in tuc')
# def step_impl(context):
#     text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[3]/th[1]").text
#
#     if text == "Totals":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check text of Credits of partner summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[2]").text

    if text == "Credits":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"