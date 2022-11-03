import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import CommonUtility as CU
tucuseridobj = CU.tucuser_id()

@then(u'Click on Add User Button')
def add_user(context):
    button = context.driver.find_element(By.ID, "create_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check the element is present')
def element_present(context):

    for element_id in tucuseridobj.tucuser_id_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)


@then(u'enter the data into given field')
def enter_data(context):
    for element_id in tucuseridobj.tucuser_id_list.keys():
        try:
            if element_id != "role_type" and element_id != "tuc" and element_id != "save_user":
                context.driver.find_element(By.ID, element_id).send_keys(tucuseridobj.tucuser_id_list[element_id])

            elif element_id == "role_type":
                role_type = context.driver.find_element(By.ID, element_id)
                select = Select(role_type)

                select.select_by_value("1112")

            elif element_id == "tuc":
                tuc = context.driver.find_element(By.ID, element_id)
                select = Select(tuc)

                select.select_by_value("2000")

            else:
                button = context.driver.find_element(By.ID,"save_user")
                context.driver.execute_script("arguments[0].click();", button)

        except NameError:
            print(NameError)

@then(u'check tuc user is created successfully or not')
def tuc_user(context):
    time.sleep(1)
    tuc_user = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if (tuc_user == "ICICIAdmin"):
        assert True, f"{tuc_user} found"
    else:
        assert False, f"{tuc_user} not found"

    # time.sleep(1)
    # context.driver.close()
