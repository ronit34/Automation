import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import CommonUtility as CU
tuc_hdfc_userobj = CU.tuc_hdfc_user()

@then(u'enter the data for HDFC User given field')
def step_impl(context):
    for element_id in tuc_hdfc_userobj.tuc_hdfc_user_list.keys():
        try:
            if element_id != "role_type" and element_id != "tuc" and element_id != "save_user":
                context.driver.find_element(By.ID, element_id).send_keys(tuc_hdfc_userobj.tuc_hdfc_user_list[element_id])

            elif element_id == "role_type":
                role_type = context.driver.find_element(By.ID, element_id)
                select = Select(role_type)

                select.select_by_value("1112")

            elif element_id == "tuc":
                tuc = context.driver.find_element(By.ID, element_id)
                select = Select(tuc)

                select.select_by_value("2001")

            else:
                button = context.driver.find_element_by_id("save_user")
                context.driver.execute_script("arguments[0].click();", button)

        except NameError:
            print(NameError)

    # time.sleep(1)
    # context.driver.close()

