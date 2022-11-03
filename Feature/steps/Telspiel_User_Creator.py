import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import Tenant_CommomUtility as CU

telspielusercreatorObj = CU.telspiel_user_creator()

telspielusercreatordropdownobj = CU.telspiel_user_creator_dropdown()


@then(u'check all elements are present in tenant user')
def check_all_elements_present(context):
    for element_id in telspielusercreatorObj.telspiel_user_creator_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")

        except NameError:
            print(NameError)

        for element_id in telspielusercreatordropdownobj.telspiel_user_creator_dropdown_inputbox_list.keys():
            try:
                status = context.driver.find_element(By.ID, element_id).is_displayed()
                print(f"{element_id} --> is {status} ")

            except NameError:
                print(NameError)


@then(u'insert input data in tenant login')
def insert_input_data(context):
    for element_id in telspielusercreatorObj.telspiel_user_creator_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            telspielusercreatorObj.telspiel_user_creator_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in telspielusercreatordropdownobj.telspiel_user_creator_dropdown_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            telspielusercreatordropdownobj.telspiel_user_creator_dropdown_inputbox_list[element_id])
        print(f"{element_id}")
    # firefox
    # accmgr = context.driver.find_element(By.ID, "tenant")
    # select = Select(accmgr)
    #
    # select.select_by_value("10")
    button = context.driver.find_element(By.ID, "tenant")
    context.driver.execute_script("arguments[0].click();", button)

    select = Select(button)

    select.select_by_visible_text("Telspiel(11)")


@then(u'check user is created or not of telspiel tenant')
def user(context):
    time.sleep(1)
    # user = context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    user = context.driver.find_element(By.XPATH,
                                       "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[1]").text

    if user == "Telspiel":
        assert True, f"{user} found"
    else:
        assert False, f"{user} not found"

    # time.sleep(2)
    # context.driver.close()
