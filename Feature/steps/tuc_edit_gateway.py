import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import CommonUtility as CU

tuc_default_gateway_dropdown_editobj = CU.tuc_default_gateway_dropdown_edit()

@then(u'check tuc edit option is present')
def edit(context):
    # edit1=context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[1]").is_displayed()
    edit1=context.driver.find_element(By.XPATH,
            "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]/img").is_displayed()
    if edit1:
        assert True, f"{edit1} found"
    else:
        assert False, f"{edit1} not found"

@then(u'check tuc delete option is present')
def delete(context):
    # delete=context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[2]").is_displayed()
    delete=context.driver.find_element(By.XPATH,
                "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[2]/img").is_displayed()
    if delete:
        assert True, f"{delete} found"
    else:
        assert False, f"{delete} not found"

@then(u'check edit icon mouse hover text - gateway edit')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    # parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[1]")
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]/img")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click on tuc edit option to change info')
def step_impl(context):
    # context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[1]").click()
    context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[1]/img").click()

@then(u'edit the default gateway as per requirements')
def step_impl(context):
    for element_id in tuc_default_gateway_dropdown_editobj.tuc_default_gateway_dropdown_edit_list.keys():
        try:
            context.driver.implicitly_wait(20)
            element_obj = context.driver.find_element(By.ID, element_id)
            context.driver.implicitly_wait(20)
            select = Select(element_obj)
            context.driver.implicitly_wait(20)
            select.select_by_visible_text(tuc_default_gateway_dropdown_editobj.tuc_default_gateway_dropdown_edit_list[element_id])
        except NameError:
            print(NameError)


@then(u'click on the tuc update button to save changes')
def click_update(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("update_tuc")
    context.driver.execute_script("arguments[0].click();", button)
    if edit:
        assert True, f"{edit} found"
    else:
        assert False, f"{edit} not found"

    # time.sleep(1)
    # context.driver.close()


