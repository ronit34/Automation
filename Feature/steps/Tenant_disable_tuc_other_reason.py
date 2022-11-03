import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'Click on action button to enable account')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
              "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[3]/td[6]/a[3]/div/label/input")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on other reason')
def step_impl(context):
    time.sleep(2)
    ele = context.driver.find_element(By.ID, "suspend_tuc")
    select = Select(ele)
    select.select_by_visible_text("Other")


@then(u'enter reason for disable')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element_by_id("other_reason").send_keys("promotes violence")

@then(u'mouse hover on disable and verify reason for disable')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[4]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]/td[4]").get_attribute('title')
    if hover_title == "Reason: promotes violence":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"
