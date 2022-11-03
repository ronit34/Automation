from selenium.webdriver import ActionChains
from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on mis web search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

    # scroll to middle of page
    context.driver.execute_script("window.scrollTo(0, 140)")

@then(u'Hover on first number under SMS Count')
def step_impl(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[10]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[10]").get_attribute('title')
    # if hover_title == "Valid No: 1\nDuplicate No: 0\nInvalid No: 0":     ##### No sequential data in MIS #######
    #     print(f"{hover_title} --> is present")
    #     print(f"{hover_title} --> is present")
    # else:
    #     assert False, f"{hover_title}--->is not present"

    # time.sleep(1)
    # context.driver.close()
