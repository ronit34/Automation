from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Check for Submitted Credits text in campaign Summary')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='v-pills-tab']/div[1]/p[1]").text
    if text == "Submitted Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Delivered Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='v-pills-tab']/div[2]/p[1]").text
    if text == "Delivered Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Failed Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='v-pills-tab']/div[3]/p[1]").text
    if text == "Failed Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Awaited Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='v-pills-tab']/div[4]/p[1]").text
    if text == "Awaited Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for TUC ID text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[1]").text
    if text == "TUC ID":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for TUC Name text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[2]").text
    if text == "TUC Name":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Campaign Name text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[3]").text
    if text == "Campaign Name":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Request Time text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[4]").text
    if text == "Request Time":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for SenderID text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[5]").text
    if text == "SenderID":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Message text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[6]").text
    if text == "Message":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Submitted/Submitted Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[7]").text
    if text == "Submitted/Submitted Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Delivered/Delivered Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[8]").text
    if text == "Delivered/Delivered Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Failed/Failed Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[9]").text
    if text == "Failed/Failed Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Awaited/Awaited Credits text in campaign Summary')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[1]/th[10]").text
    if text == "Awaited/Awaited Credits":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"
