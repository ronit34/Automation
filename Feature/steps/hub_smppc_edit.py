from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import Tenant_CommomUtility as CU

hub_smppc_editobj = CU.hub_smppc_edit()

hub_smppc_dropdown_editobj = CU.hub_smppc_dropdown_edit()

@then(u'check edit option is present in SMPPC')
def check_edit_present(context):
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[3]").is_displayed()

@then(u'check delete option is present in SMPPC')
def check_delete_present(context):
    context.driver.find_element_by_css_selector("[title*='Delete']").is_displayed()


@then(u'check edit icon mouse hover text - smppc')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[3]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[3]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on edit option to change info in SMPPC')
def step_impl(context):
    button = context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[5]/a[3]")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    for element_id in hub_smppc_editobj.hub_smppc_edit_list.keys():
        text=context.driver.find_element(By.ID, element_id)
        text.clear()
        context.driver.find_element(By.ID, element_id).send_keys(
            hub_smppc_editobj.hub_smppc_edit_list[element_id])
        print(f"{element_id}")

    for element_id in hub_smppc_dropdown_editobj.hub_smppc_dropdown_edit_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(hub_smppc_dropdown_editobj.hub_smppc_dropdown_edit_list[element_id])
        except NameError:
            print(NameError)

@then(u'click on the update to save changes in SMPPC')
def step_impl(context):
    button = context.driver.find_element(By.ID, "update_smppc")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
