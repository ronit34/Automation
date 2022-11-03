from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'Check Delete Labels')
def step_impl(context):
    time.sleep(1)
    # text1 = context.driver.find_element_by_xpath(
    #    "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    text1 = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[3]/div/div/div/div[2]/p[2]").text
    if (text1 == "Are you sure want to delete?"):
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@then(u'check delete icon mouse hover text - URL')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'Click on Delete button of pop up')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "delete").click()

    # time.sleep(1)
    # context.driver.close()
