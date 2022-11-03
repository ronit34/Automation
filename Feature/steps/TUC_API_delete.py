from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'check delete icon mouse hover text - API')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[7]/a")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[7]/a").get_attribute('title')
    if hover_title == "Delete":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"


@then(u'click on the delete icon')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[7]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check whether delete pop is appeared')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/p[2]").text
    if text == "Are you sure want to delete API?":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on the delete button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[3]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(2)
    # context.driver.close()