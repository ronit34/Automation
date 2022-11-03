from behave import *
from selenium.webdriver.common.by import By
import time

import CommonUtility as CU
Edit_NotificationObj=CU.Edit_Notification

@then(u'click on Edit')
def step_impl(context):
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table[2]/tbody/tr[2]/td[5]/a[1]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'edit data into Notification fields')
def step_impl(context):
    time.sleep(4)

    context.driver.find_element(By.ID,"noitf_sub").clear()
    context.driver.find_element(By.ID, "noitf_text").clear()

    for element_id in Edit_NotificationObj.Edit_Notification_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(Edit_NotificationObj.Edit_Notification_inputbox_list[element_id])

@then(u'click on Update btn to update')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID,"update")
    context.driver.execute_script("arguments[0].click();", button)