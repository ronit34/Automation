from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'check delete icon mouse hover text - blacklist_category')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='delete']")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='delete']").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'CLick on delete of created blacklist category')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='delete']/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Check Message of delete pop up')
def step_impl(context):
    time.sleep(2)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[3]/div/div/div/div[2]/p[1]").text

    if text == "Name : Fresh":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'Click on delete button to delete category')
def step_impl(context):
    time.sleep(4)
    button = context.driver.find_element(By.XPATH,
           "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Check selected blacklist category is deleted or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath(
        "//*[@id='tab_content']/table/tbody/tr[2]/td[2]").text
    if text != "Fresh [1405]":
        assert True, f"{text} is not present"
    else:
        assert False, f"{text} is present present"

    # time.sleep(1)
    # context.driver.close()