from behave import *
import time

from selenium.webdriver.common.by import By


@then(u'Click on Spam')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_spam']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Spam header')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text
    if text == "SPAM":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check text of Spam Category')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("spam_cat").text
    if text == "Spam Category":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check text of Keywords')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("spam_keywords").text
    if text == "Keywords":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'check text of Category Assign')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("spam_assign").text
    if text == "Category Assign":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Click on Spam Category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("spam_cat")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Category Name tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='tab_content']/table/tbody/tr[1]/th[1]").text
    if text == "Category Name":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Action tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='tab_content']/table/tbody/tr[1]/th[2]").text
    if text == "Action":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check text of Add Category Button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add-spam-cat").text
    if text == "+ Add Category":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Click on add Category Button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add-spam-cat")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Add Spam Category')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[1]/p[1]").text
    if text == "Add Spam Category":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Category Text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div/label").text

    # if text == "Category":
    if text == "Category*":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Cancel Buttn')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("cancel").get_attribute("value")
    if text == "Cancel":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Add Button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add").get_attribute("value")
    if text == "Add":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Click on Cross Button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[1]/input")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on Keywords tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("spam_keywords")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Select Category text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div[1]/label").text

    # if text == "Select Category":
    if text == "Select Category*":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for search text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("search").get_attribute("value")
    if text == "Search":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Add Keywords text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add-spam-keywords").text
    if text == "+ Add Keywords":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Click on Add Keywords')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "add-spam-keywords")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Add Spam Category text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[1]/p[1]").text
    # if text == "Add Spam Category":
    if text == "Add Spam Keywords":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Spam Keywords text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/label").text
    # if text == "Spam Keywords":
    if text == "Spam Keywords*":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Check for Add Keywords text button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("split_more").text
    if text == "+ Add Keywords":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"

@then(u'Click on Category Assign tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("spam_assign")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check for Add TUCs text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add-spam-tuc").text
    if text == "+ Add TUCs":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Click on Add TUCs')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add-spam-tuc")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check for Add TUCs')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[1]/p").text
    if text == "Add TUCs":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Check for select category')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/label").text

    # if text == "Select Category":
    if text == "Select Category*":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"


@then(u'Check for TUCs')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/label").text
    if text == "TUCs":
        assert True, "Text Passed"
    else:
        assert False, f" {text} ----> Not Found"