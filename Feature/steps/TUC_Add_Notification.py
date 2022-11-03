from selenium.webdriver.common.by import By
import time
from behave import *

import CommonUtility as CU
Tuc_Add_NotificationObj = CU.Tuc_Add_Notification()

@then(u'insert data into Tuc Notification fields')
def step_impl(context):
    time.sleep(2)
    for element_id in Tuc_Add_NotificationObj.Tuc_Add_Notification_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Tuc_Add_NotificationObj.Tuc_Add_Notification_inputbox_list[element_id])
