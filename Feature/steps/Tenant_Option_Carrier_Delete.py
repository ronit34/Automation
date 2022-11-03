from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

@then(u'check delete icon is present of first carrier')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]/a[2]/img").is_displayed()


@then(u'check delete icon mouse hover text - carrier')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on delete icon of first carrier')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[3]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if popup is appear or not')
def step_impl(context):
    time.sleep(1)
    a = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div[1]/div/div/div/div[1]/p[1]").is_displayed()
    if a:
        assert True, f"{a} is present"
    else:
        assert False, f"{a} is not present"

@then(u'click on delete button inside carrier tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div[1]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'verify the carrier is deleted or not')
def step_impl(context):
    time.sleep(1)
    try:
        context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[1]")
        assert False, "Carrier is not deleted"
    except NoSuchElementException:
        time.sleep(2)
        assert True, "Carrier is deleted"

    # time.sleep(2)
    # context.driver.close()

