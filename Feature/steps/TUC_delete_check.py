import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import CommonUtility as CU
tuc_deleteObj = CU.tuc_delete()

@then(u'check TUC is present there')
def tuc_present(context):
    time.sleep(1)
    tuc=context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[1]").text
    if tuc=="ICICI(2000)":
        assert True, f"{tuc} is present"
    else:
        assert False, f"{tuc} is not present"


@then(u'check delete icon mouse hover text - tuc')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    # parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[2]")
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'check TUC is able to delete or not by clicking on delete option')
def click_delete(context):
    # context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[2]").click()
    context.driver.find_element(By.XPATH,"//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[6]/a[2]/img").click()

@then(u'chekc error label is present')
def check_error_msg(context):
    for x in tuc_deleteObj.tuc_delete_list:
        try:
            status = context.driver.find_element(By.XPATH, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check error message is present')
def check_error_label(context):
    for x in tuc_deleteObj.tuc_delete_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == tuc_deleteObj.tuc_delete_list[x]:
            print(f"{tuc_deleteObj.tuc_delete_list[x]}--> found")
        else:
            print(f"{tuc_deleteObj.tuc_delete_list[x]}--> Not found")

@then(u'click on close button')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/div/div/div/div/div[3]/a").click()

    # time.sleep(1)
    # context.driver.close()