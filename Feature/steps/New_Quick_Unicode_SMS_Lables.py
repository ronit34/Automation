import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'click on Quick Unicode/Multilingual SMS')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element_by_xpath("//*[@id='unicode_sms_page_link']/img")
    button = context.driver.find_element_by_xpath("//*[@id='unicode_sms_page_link']/div/img[1]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if New SMS/Unicode SMS text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "New SMS/Unicode SMS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select unicode template from Select Template dropdown')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('template_name'))
    # select.select_by_value('1303')
    select.select_by_visible_text('Hindi One Variable')            #### Hindi One Var ####

@then(u'check if Allow Unicode text is present or not in quick sms')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[2]").text

    if text == "Allow Unicode":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'select the Allow Unicode checkbox')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input")
    context.driver.execute_script("arguments[0].click();", button)



