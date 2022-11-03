from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
Add_NotificationObj = CU.Add_Notification()

@then(u'check Notification is present')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='menu_notification']/p").text

    if text == "Notification":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Notification')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_notification']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Notification Subject text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr/th[1]").text

    if text == "Subject":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Notification Content text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr/th[2]").text

    if text == "Content":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Notification Applicable To Subject text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr/th[3]").text

    if text == "Applicable To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Notification Created at text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr/th[4]").text

    if text == "Created at":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Notification Action text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr/th[5]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Click on Add Notification')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add_notification")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check if Add Notification text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "notification_title").text

    if text == "Add Notification":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check if Subject text is present or not in pop up')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[1]/label").text

    if text == "Subject*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check if Content text is present or not in pop up')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[2]/label").text

    if text == "Content*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check if Applicable To text is present or not in pop up')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='myModal']/div/div/div[2]/div[3]/label").text

    if text == "Applicable To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'Check if Add text is present or not in pop up')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "add").get_attribute("value")

    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
