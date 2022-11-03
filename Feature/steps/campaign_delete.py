from behave import *
import time

from selenium.webdriver import ActionChains


@then(u'check delete icon is present inside campaign tab')
def check_delete_icon(context):
    time.sleep(1)
    context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[4]/td[4]/a[2]/img").is_displayed()


@then(u'check delete icon mouse hover text - campaign')
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


@then(u'click on delete icon inside campaign tab')
def click_delete_icon(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[4]/td[4]/a[2]/img")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check popup appear or not in campaign tab')
def check_popup(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[3]/div/div/div/div[1]/p[1]").text
    if text == "Caution":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on delete button inside campaign tab')
def click_delete_button(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[3]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()