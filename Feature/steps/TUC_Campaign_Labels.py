import time
from behave import *
from selenium.webdriver.common.by import By

@then(u'click on the campaign tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("menu_campaigns")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Campaign header text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "Campaign":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Campaign Name sub header text is present or not in tuc campaign')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[2]").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]").text

    if text == "Campaign Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description sub header text is present or not in tuc campaign')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[3]").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]").text

    if text == "Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action sub header text is present or not in tuc campaign')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[1]/th[4]").text
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[4]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add campaign button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("create_campaign")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Add Campaign text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[1]/p[1]").text

    if text == "Add Campaign":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check for Campaign Name text inside add campaign button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Campaign Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check for Description text inside add campaign button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    if text == "Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of add button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='add_campaign']").get_attribute('value')

    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of cancel button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel_modal']").get_attribute('value')

    if text == "Cancel":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()