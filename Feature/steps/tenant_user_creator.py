import time
from telnetlib import EC

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

class ExpectedConditions:
    pass

from selenium.webdriver.support import expected_conditions as EC

import CommonUtility as CU

usercreatorObj = CU.user_creator()

usercreatordropdownobj = CU.user_creator_dropdown()

@then(u'check Bell Icon present')
def bell_icon(context):
    status = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/img").is_displayed()
    assert status is True
    print(f"{status}:Bell Icon is present")

@then(u'check Date present on the page')
def date(context):
    status = context.driver.find_element(By.XPATH, " /html/body/div[1]/div[2]/div[3]/div[1]/p[2]").is_displayed()
    assert status is True
    print(f"{status}:right date is present")

@then(u'click on User')
def click_user(context):
    context.driver.find_element(By.ID, "user_view").click()


@then(u'check add user button')
def add_user(context):
    try:
       WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "create_user")))
    except NameError:
        print("the element is not visiable ")

@then(u'click on add user')
def click_add(context):
    button = context.driver.find_element(By.ID, "create_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check all elements are present')
def check_all_elements_present(context):

    for element_id in usercreatorObj.user_creator_inputbox_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
           
        except NameError:
            print(NameError)

        for element_id in usercreatordropdownobj.user_creator_dropdown_inputbox_list.keys():
            try:
                status = context.driver.find_element(By.ID, element_id).is_displayed()
                print(f"{element_id} --> is {status} ")
                
            except NameError:
                print(NameError)
            
@then(u'insert input data')
def insert_input_data(context):

    for element_id in usercreatorObj.user_creator_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            usercreatorObj.user_creator_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in usercreatordropdownobj.user_creator_dropdown_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(usercreatordropdownobj.user_creator_dropdown_inputbox_list[element_id])
        print(f"{element_id}")
    #firefox
    # accmgr = context.driver.find_element(By.ID, "tenant")
    # select = Select(accmgr)
    #
    # select.select_by_value("10")
    button = context.driver.find_element(By.ID, "tenant")
    context.driver.execute_script("arguments[0].click();", button)

    select = Select(button)

    select.select_by_value("10")

@then(u'click on create Button')
def click_create(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "save_user")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check user is created or not')
def user(context):
    time.sleep(2)
    user = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if (user == "Onexadmin"):
        assert True, f"{user} found"
    else:
        assert False, f"{user} not found"

    # time.sleep(1)
    # context.driver.close()

