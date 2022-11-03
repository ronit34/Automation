from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import CommonUtility as CU
DLTsenderIDObj = CU.DLT_senderID()

@then(u'check edit icon mouse hover text - SenderID')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[2]/td[7]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='senderid_table']/tbody/tr[2]/td[7]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on edit icon in SenderID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='senderid_table']/tbody/tr[2]/td[7]/a[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'change the Entity name')
def step_impl(context):
    entity = context.driver.find_element(By.ID, "sender_entity_id")
    select = Select(entity)

    select.select_by_visible_text("OTPL(456)")

@then(u'Click on Update in edit senderID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/input[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(3)
    # context.driver.close()


