from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU
Add_NotificationObj = CU.Add_Notification()

@then(u'select dropdown tuc "Tenant/TUC with children"')
def step_impl(context):
    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "applicable_to")
    select = Select(button1)
    select.select_by_visible_text("Tenant/TUC with children")

@then(u'insert data into Notification fields')
def step_impl(context):
    time.sleep(2)
    for element_id in Add_NotificationObj.Add_Notification_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Add_NotificationObj.Add_Notification_inputbox_list[element_id])

@then(u'check Notification is created or not')
def step_impl(context):
    time.sleep(3)
    txt = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[2]/table[2]/tbody/tr[2]/td[1]").text

    print(f"{txt}")
    print(f"{txt}")

    time.sleep(2)
    if txt == "adding notification":
        assert True, "Notification found"
    else:
        assert False, "Notification Not found"
