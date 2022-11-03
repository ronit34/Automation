from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'check delete icon mouse hover text - entityID')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on delete icon against entityID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='entityid_table']/tbody/tr[2]/td[3]/a[2]").click()


@then(u'check error label in popup')
def step_impl(context):
    time.sleep(1)
    entityID = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[2]/p[1]").text
    label = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/div/div/div/div[2]/p[2]").text

    if (entityID == "Entity ID : onextel" and label == "Are you sure want to delete?"):
        assert True, f"{entityID} --> label present"
    else:
        assert False, f"{entityID} ----> label absent"


@then(u'click on Delete Button to delete EntityID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "delete").click()

    # time.sleep(3)
    # context.driver.close()