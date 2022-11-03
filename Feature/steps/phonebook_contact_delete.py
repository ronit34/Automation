from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

@then(u'check delete icon is present or not')
def check_delete_icon(context):
    time.sleep(1)
    context.driver.find_element_by_css_selector(
        "[title*='Delete']").is_displayed()


@then(u'check delete icon mouse hover text - contact')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    # parent_level_menu = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[4]/a[2]")
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[5]/a[2]/img")
    action.move_to_element(parent_level_menu).perform()

    # hover_title = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[4]/a[2]").get_attribute('title')
    hover_title = context.driver.find_element_by_xpath("//*[@id='contacts-table']/tbody/tr[2]/td[5]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on delete icon')
def click_delete_icon(context):
    time.sleep(1)
    button = context.driver.find_element_by_css_selector("[title*='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check popup appear or not')
def check_popup(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/div/div/div/div[2]/p").text
    # if text == "Are you sure want to delete?":
    # if text == "Name :william , Are you sure want to delete?":
    if text == "Name :william":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on delete button inside contact tab')
def click_delete_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("delete")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
