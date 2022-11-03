from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'select campaign name and sender id')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "campaign_name"))
    select.select_by_visible_text('default(2200)')
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "sender_id"))
    select.select_by_visible_text('123456')

@then(u'select new group')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "groupDropdown"))
    select.select_by_visible_text('campaign (1)')

@then(u'check the scheduled sms is present or not')
def step_impl(context):
    time.sleep(2)
    schedule = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div/table/tbody/tr[2]/td[1]").text
    if schedule == '123456':
        assert True, f"Scheduled sms is present"
    else:
        assert False, f"Scheduled sms is not present"

    # time.sleep(1)
    # context.driver.close()




