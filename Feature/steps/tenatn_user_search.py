from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@then(u'check error label of user search')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "user_input").send_keys("z")

    time.sleep(1)
    context.driver.find_element(By.ID, "user_search").click()

    time.sleep(1)

    a=context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/span").text
    if a == "No Record found : z":
        assert True, f"{a} is present"
    else:
        assert False, f"{a} is not present"

    # time.sleep(1)
    # context.driver.close()