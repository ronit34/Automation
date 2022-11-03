import time
from behave import *
from selenium import *

@then(u'click on DLT Management')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/a[1]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[1]/div[2]/a[1]/div/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'go to dashboard')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("menu_dashboard")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Schedule campaigns quick stats')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/a[2]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[1]/div[2]/a[2]/div/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify redirected page in reports')
def step_impl(context):
    text = context.driver.find_element_by_id("pills-campaign-tab").text

    if text == "Scheduled Campaigns":
        assert True, f"{text} is present"
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on sender id quick stats')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/a[3]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[1]/div[2]/a[3]/div/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on template quick stats')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[1]/div[2]/a[4]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[1]/div[2]/a[4]/div/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify redirected template tab heading')
def step_impl(context):
    text = context.driver.find_element_by_id("template_tab").text

    if text == "Template":
        assert True, f"{text} is present"
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
##################
@then(u'click on contacts quick shortcut')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[2]/div[2]/a[1]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[2]/div[2]/a[1]/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify redirected to contacts tab')
def step_impl(context):
    text = context.driver.find_element_by_id("contacts").text

    if text == "Contacts":
        assert True, f"{text} is present"
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on groups quick shortcut')
def step_impl(context):
    # scroll to bottom of page
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(2)
    button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[6]/div[2]/div[2]/a[2]/div")
    # button = context.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[7]/div[2]/div[2]/a[2]/div/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify redirected to groups tab')
def step_impl(context):
    text = context.driver.find_element_by_id("groups").text

    if text == "Groups":
        assert True, f"{text} is present"
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
