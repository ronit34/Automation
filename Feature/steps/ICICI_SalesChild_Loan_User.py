import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import TUC_CommonUtility as CU
Sales_child_loan_userobj = CU.Sales_child_loan_user()

@then(u'check the element is present in sales tuc in user tab')
def element_present(context):

    for element_id in Sales_child_loan_userobj.Sales_child_loan_user_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'enter the data into given field in sales tuc in user tab')
def enter_data(context):
    for element_id in Sales_child_loan_userobj.Sales_child_loan_user_list.keys():
        try:
            if element_id != "role_type" and element_id != "tuc" and element_id != "save_user":
                context.driver.find_element(By.ID, element_id).send_keys(Sales_child_loan_userobj.Sales_child_loan_user_list[element_id])

            elif element_id == "role_type":
                role_type = context.driver.find_element(By.ID, element_id)
                select = Select(role_type)

                select.select_by_value("1112")

            elif element_id == "tuc":
                tuc = context.driver.find_element(By.ID, element_id)
                select = Select(tuc)
                #28th Feb
                select.select_by_value("2003")
                #19th Aug
                # select.select_by_value("2005")

            else:
                button = context.driver.find_element_by_id("save_user")
                context.driver.execute_script("arguments[0].click();", button)

        except NameError:
            print(NameError)

@then(u'check tuc user credit is created successfully or not')
def tuc_user(context):
    time.sleep(1)
    tuc_user = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if (tuc_user == "loan"):
        assert True, f"{tuc_user} found"
    else:
        assert False, f"{tuc_user} not found"

    # time.sleep(1)
    # context.driver.close()