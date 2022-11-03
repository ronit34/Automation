from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU

DLT_searchObj = CU.DLT_search()

@then(u'go to search tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on search in dlt search tab')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element_by_id("template_search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check error label')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div").text
    if text == "Please Enter Template Name/ID":
        assert True, f"{text}  ---->  present"
    else:
        assert False, f" {text} ----> not present"

@then(u'enter 3 characters and check error label')
def step_impl(context):
    time.sleep(1)
    search_text = context.driver.find_element(By.ID, "enter_type").send_keys("eng")

    time.sleep(2)
    temp = context.driver.find_element(By.ID, "template_type")
    select = Select(temp)
    select.select_by_visible_text("Template Name")

    time.sleep(2)
    button = context.driver.find_element_by_id("template_search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div").text
    if text == "Enter atleast 4 characters":
        assert True, f"{text}  ---->  present"
    else:
        assert False, f" {text} ----> not present"

@then(u'input full Template name')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    search_text = context.driver.find_element(By.ID, "enter_type").send_keys("english long")

    # time.sleep(2)
    # temp = context.driver.find_element(By.ID, "template_type")
    # select = Select(temp)
    # select.select_by_visible_text("Template Name")

    time.sleep(2)
    button = context.driver.find_element_by_id("template_search")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(4)
    for x in DLT_searchObj.DLT_search_list:
        # context.driver.implicitly_wait(20)
        time.sleep(3)
        if context.driver.find_element(By.XPATH, x).text != DLT_searchObj.DLT_search_list[x]:
            print(f"{DLT_searchObj.DLT_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div").text
            if text1 == "No Record Found":
                time.sleep(2)
                assert True, f"{text1}  ---->  present"
            else:
                assert False, f" {text1} ----> not present"
        else:
            print(f"{DLT_searchObj.DLT_search_list[x]}-->  found")

    # time.sleep(1)
    # context.driver.close()
