from behave import *
import time

# from selenium import webdriver

@then(u'click on telco reports')
def step_impl(context):

    time.sleep(1)
    context.driver.find_element_by_id("menu_telco_reports").click()

@then(u'check text of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_id("partner-tab").text

    if text == "Partner Summary":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of From of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[1]/div[1]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of To of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[1]/div[2]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Search Button of partner')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_id("search").get_attribute("value")

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on Search of partner summary')
def step_impl(context):
    # time.sleep(1)
    context.driver.find_element_by_id("search").click()

@then(u'check text of TUC NAME of partner summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[1]").text

    if text == "TUC NAME":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Submitted of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[2]").text

    if text == "Submitted":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Delivered of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[3]").text

    if text == "Delivered":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Failed of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[4]").text

    if text == "Failed":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Awaited of partner summary')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[1]/th[5]").text

    if text == "Awaited":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Totals of partner summary in tenant')
def step_impl(context):
    # time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='partners']/tbody/tr[4]/th[1]").text

    if text == "Totals":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
