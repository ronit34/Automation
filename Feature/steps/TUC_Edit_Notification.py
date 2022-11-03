import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import *

import CommonUtility as CU
Tuc_Edit_NotificationObj=CU.Tuc_Edit_Notification

@then(u'edit data into Tuc Notification fields')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.ID,"noitf_sub").clear()
    context.driver.find_element(By.ID, "noitf_text").clear()
    for element_id in Tuc_Edit_NotificationObj.Tuc_Edit_Notification_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(Tuc_Edit_NotificationObj.Tuc_Edit_Notification_inputbox_list[element_id])