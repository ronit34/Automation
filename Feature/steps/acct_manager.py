from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

class manager_creator:
    manager_creator_inputbox_list = {}
    manager_creator_inputbox_list['username'] = "sant"
    manager_creator_inputbox_list['password'] = "ali"
    manager_creator_inputbox_list['fname'] = "sant"
    manager_creator_inputbox_list['lname'] = "singh"
    manager_creator_inputbox_list['email'] = "sant@"
    manager_creator_inputbox_list['mob_no'] = "8"
    manager_creator_inputbox_list['comp_name'] = "OneXtel"
    manager_creator_inputbox_list['web'] = "onextel.tech"
    manager_creator_inputbox_list['other_mob_no'] = "3"
    manager_creator_inputbox_list['cancel'] = "Button"
    manager_creator_inputbox_list['save_user'] = "Button"

# ************************* Code For Dropdown **********************************
    manager_creator_dropdown = {}
    manager_creator_inputbox_list['role_type'] = "Manager"
    manager_creator_inputbox_list['role_type'] = "Manager"


@then(u'Click on User Button')
def step_impl(context):
    context.driver.find_element(By.ID, "user_view").click()

# @when(u'Click on add User Button')
# def add_user(context):
#     context.driver.find_element(By.ID, "create_user").click()
    
@then(u'insert element')
def step_impl(context):
    manager_creator_obj = manager_creator()
    for element_id in manager_creator_obj.manager_creator_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            manager_creator_obj.manager_creator_inputbox_list[element_id])
        print(f"{element_id}")

    for element_id in manager_creator_obj.manager_creator_dropdown.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(manager_creator_obj.manager_creator_dropdown[element_id])

        except NameError:
            print(NameError)


@then(u'click on Create')
def step_impl(context):
    button = context.driver.find_element_by_id("save_user")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check manger is created or not')
def manager(context):
    time.sleep(1)
    manager = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if (manager == "sant"):
        assert True, f"{manager} found"
    else:
        assert False, f"{manager} not found"

    # time.sleep(1)
    # context.driver.close()



