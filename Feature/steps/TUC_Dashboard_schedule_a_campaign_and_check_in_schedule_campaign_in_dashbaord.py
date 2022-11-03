from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


@then(u'select campaign_name and sender_id')
def step_impl(context):
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "campaign_name"))
    select.select_by_visible_text('default(2200)')
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "sender_id"))
    select.select_by_visible_text('123456')


@then(u'select new_group for campaign')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "groupDropdownCamp"))
    select.select_by_visible_text('campaign (1)')


@then(u'Click on Send NOW_Button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Dashboard')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_dashboard']/p")
    context.driver.execute_script("arguments[0].click();", button)
    context.driver.refresh()
    time.sleep(2)


@then(u'Click on Dashboard Scheduled SMS')
def step_impl(context):
    time.sleep(2)
    context.driver.refresh()
    button = context.driver.find_element(By.ID, "collapsable_schedule")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)


@then(u'Check seheduled sms is present or not')
def step_impl(context):
    time.sleep(2)
    schedule = context.driver.find_element(By.XPATH, '//*[@id="dashboard_table"]/tbody/tr[3]/td[1]').text
    if schedule == 'default':
        assert True, f"Scheduled sms is present"
    else:
        assert False, f"Scheduled sms is not present"
