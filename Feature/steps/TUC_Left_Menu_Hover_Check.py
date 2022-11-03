from behave import *
import time
from selenium.webdriver import ActionChains

@then(u'Click on Arrow symbol')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("arrow")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Hover on Dashboard and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_dashboard']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_dashboard']/img").get_attribute('title')
    if hover_title == "Dashboard":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Campaign and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_campaigns']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_campaigns']/img").get_attribute('title')
    if hover_title == "Campaign":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on User Management and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_users']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_users']/img").get_attribute('title')
    if hover_title == "User Management":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Credits and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_credit_allocation']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_credit_allocation']/img").get_attribute('title')
    if hover_title == "Credits":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Reports and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_report']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_report']/img").get_attribute('title')
    if hover_title == "Reports":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Telco Reports and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_telco_reports']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_telco_reports']/img").get_attribute('title')
    if hover_title == "Telco Reports":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on DLT and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_manage']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_manage']/img").get_attribute('title')
    if hover_title == "DLT":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on SMPP and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_smpps_view']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_smpps_view']/img").get_attribute('title')
    if hover_title == "SMPP":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on API and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_api']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_api']/img").get_attribute('title')
    if hover_title == "API":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

    # scroll to middle of page
    context.driver.execute_script("window.scrollTo(0, 187)")

# @then(u'Hover on Approvals and check text')
# def step_impl(context):
#     time.sleep(2)
#     action = ActionChains(context.driver);
#     parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_approvals']/img")
#     action.move_to_element(parent_level_menu).perform()
#
#     hover_title = context.driver.find_element_by_xpath("//*[@id='menu_approvals']/img").get_attribute('title')
#     if hover_title == "Approvals":
#         print(f"{hover_title} --> is present")
#         print(f"{hover_title} --> is present")
#     else:
#         assert False, f"{hover_title}--->is not present"

@then(u'Hover on Phonebook and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_phonebook']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_phonebook']/img").get_attribute('title')
    if hover_title == "Phonebook":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Config and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_config']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_config']/img").get_attribute('title')
    if hover_title == "Config":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Hover on Notification and check text')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='menu_notification']/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='menu_notification']/img").get_attribute('title')
    if hover_title == "Notification":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

    # time.sleep(1)
    # context.driver.close()
