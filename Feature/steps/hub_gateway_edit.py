from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU
hub_gateway_editobj = CU.hub_gateway_edit()

hub_gateway_dropdown_editobj = CU.hub_gateway_dropdown_edit()
@then(u'check edit option is present')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]").is_displayed()

@then(u'check delete option is present')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]").is_displayed()


@then(u'check edit icon mouse hover text - gateway')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on edit option to change info')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]").click()
    time.sleep(1)
    for element_id in hub_gateway_editobj.hub_gateway_edit_list.keys():
        text=context.driver.find_element(By.ID, element_id)
        text.clear()
        context.driver.find_element(By.ID, element_id).send_keys(hub_gateway_editobj.hub_gateway_edit_list[element_id])
        print(f"{element_id}")

    for element_id in hub_gateway_dropdown_editobj.hub_gateway_dropdown_edit_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(hub_gateway_dropdown_editobj.hub_gateway_dropdown_edit_list[element_id])
        except NameError:
            print(NameError)

@then(u'click on the update to save changes')
def step_impl(context):
        context.driver.find_element(By.ID, "update_gateway").click()

        # time.sleep(1)
        # context.driver.close()

