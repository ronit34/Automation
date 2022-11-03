from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time

@then(u'check delete icon is present in group tab')
def check_delete_icon(context):
    time.sleep(1)
    text = context.driver.find_element_by_css_selector("[title*='Delete']").is_displayed()
    if text:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check delete icon mouse hover text - final_delete')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[4]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[4]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on delete icon in group tab')
def click_delete_icon(context):
    time.sleep(1)
    button = context.driver.find_element_by_css_selector("[title*='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if warning message present in group tab')
def check_message(context):
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]").text
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[1]/p[1]").text
    # if text == "Warning!":
    if text == "Warning":
        time.sleep(1)
        button = context.driver.find_element_by_id("cancel")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        time.sleep(2)
        button = context.driver.find_element_by_id("delete")
        context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
