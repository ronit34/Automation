import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'Click on edit button of ICICI')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
            "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Select mask number as NO')
def step_impl(context):
    time.sleep(1)
    ele = context.driver.find_element(By.ID, "mask_phone")
    select = Select(ele)
    select.select_by_visible_text("No")

@then(u'click on update button to update mask number')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "update_tuc")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
