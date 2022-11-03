from behave import *
import time

from selenium.webdriver import ActionChains


@then(u'check delete icon mouse hover text - SA_category')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[2]/a[2]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr[2]/td[2]/a[2]").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'click   Delete')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("add")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
