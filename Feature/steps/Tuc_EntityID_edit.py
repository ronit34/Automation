from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'insert values in entity fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "entity_id").send_keys("456")
    time.sleep(2)
    context.driver.find_element(By.ID, "entity_name").send_keys("qwerty")

@then(u'check edit icon mouse hover text - entityID')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on edit icon')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[1]").click()


@then(u'update values in entity fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "entity_name").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "entity_name").send_keys("OTPL")


@then(u'click on update')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "update_entityid").click()



@then(u'check the updated entity id')
def step_impl(context):
    time.sleep(1)
    entityID = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[1]").text
    entityName = context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[2]").text

    if (entityID == "456" and entityName == "OTPL"):
        assert True, f"{entityID} updated successfully"
    else:
        assert False, f"{entityID} not updated , Test Failed"

    # time.sleep(2)
    # context.driver.close()