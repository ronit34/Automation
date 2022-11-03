import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'check if New SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "New SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Choose SMS Type text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/p[1]").text

    if text == "Choose SMS Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Quick English SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[2]/div/div[1]/div/p[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='quick_sms_page_link']/div/div/p[1]").text

    if text == "Quick English SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Quick Unicode/Multilingual SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[2]/div/div[2]/div/p[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='unicode_sms_page_link']/div/div/p[1]").text

    if text == "Quick Unicode/Multilingual SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Dynamic SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[2]/div/div[3]/div/p[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='dynamic_sms_page_link']/div/div/p[1]").text

    if text == "Dynamic SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Campaign SMS text is present or not')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[2]/div/div[4]/div/p[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='campaign_sms_page_link']/div/div/p[1]").text

    if text == "Campaign SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()