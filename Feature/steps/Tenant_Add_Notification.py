import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support.select import Select

import CommonUtility as CU
Add_NotificationObj = CU.Add_Notification()

@then(u'select dropdown tuc "{TUC}"')
def step_impl(context,TUC):
    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "applicable_to")
    select = Select(button1)
    select.select_by_visible_text("TUC with children")