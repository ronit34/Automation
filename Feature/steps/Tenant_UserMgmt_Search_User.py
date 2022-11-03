from behave import *
import time
from selenium.webdriver.common.by import By

@then(u'switch to user')
def user(context):
    time.sleep(1)
    context.driver.find_element_by_id("user_view").click()

@then(u'search for the user "Sant"')
def search_user(context):
    # context.driver.find_element(By.ID,"user_input").send_keys("sant")
    context.driver.find_element(By.ID,"user_input").send_keys("ICICIAdmin")

@then(u'click on the search button')
def click_search(context):
    context.driver.find_element(By.ID,"user_search").click()

@then(u'finally check if the search field is present or not')
def step_impl(context):
    time.sleep(3)
    user = context.driver.find_element(By.XPATH,
            "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[2]/td[1]").text
    if user=="ICICIAdmin":
        assert True, f"{user} found"
    else:
        assert False, f"{user} not found"

    # time.sleep(1)
    # context.driver.close()
