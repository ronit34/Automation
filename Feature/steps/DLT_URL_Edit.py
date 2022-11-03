from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@then(u'check edit icon mouse hover text - dlt url')
def check_edit_button(context):
    time.sleep(2)
    action = ActionChains(context.driver);
    parent_level_menu = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]")
    action.move_to_element(parent_level_menu).perform()

    hover_title = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]").get_attribute('title')
    if hover_title == "Edit":
        print(f"{hover_title} --> is present")
        print(f"{hover_title} --> is present")
    else:
        assert False, f"{hover_title}--->is not present"

@then(u'Click on Edit icon of URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[4]/a[1]/img").click()


@then(u'Check Edit Labels')
def step_impl(context):
    text1 = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]/p[1]").text
    text2 = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/label").text
    # if (text1 == "Edit URL" and text2 == "URL *"):
    if (text1 == "Edit Short URL" and text2 == "URL *"):
        assert True, "Test Passed"
    else:
        assert False, "Test Failed"


@then(u'Insert data into Update URL fields')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/input").clear()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/input").send_keys("facebook.com")


@then(u'click on Update button to add URL')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/input[2]").click()


@then(u'Check URL is edited or not')
def step_impl(context):
    time.sleep(1)
    entity = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[2]").text
    if (entity == "facebook.com"):
        assert True, f"{entity} found"
    else:
        assert False, f"{entity} not found"

    # time.sleep(1)
    # context.driver.close()
