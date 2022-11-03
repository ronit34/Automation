from behave import *
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU

User_Mgmt_searchObj = CU.User_Mgmt_search()

from selenium.webdriver.support.select import Select


@then(u'click on Search Tab in DLT')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'input SenderID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "enter_type").send_keys("123456")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('Sender ID')


@then(u'click on search and check if data is present')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/h5").text
            if text1 == "SenderId Info":
                time.sleep(2)
                rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div[1]/table/tbody/tr")
                x = len(rows) - 1
                assert True, f" {x} ----> rows present"
            else:
                assert False, f" No data Present , Test Failed"

            time.sleep(1)
            # text2 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/h5").text
            text2 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[3]/h5").text
            if text2 == "TUC Hierarchy(2000)":
                assert True, f" {text2} ---->  present"
            else:
                assert False, f" {text2} ----> Not Found , Test Failed"

            time.sleep(1)
            # text3 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[3]/h5").text
            text3 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/h5").text
            if text3 == "TUC Hierarchy(2001)":
                assert True, f" {text3} ----> present"
            else:
                assert False, f" {text3}-----> not found , Test Failed"


        else:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}-->  found")


@then(u'input SystemID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").send_keys("2")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('System ID')


@then(u'click on search and check if data is present SystemID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/h5").text
            if text1 == "SMPP Info":
                time.sleep(2)
                rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div[1]/table/tbody/tr")
                x = len(rows) - 1
                assert True, f" {x} ----> rows present"
            else:
                assert False, f" No data Present , Test Failed"

            time.sleep(1)
            text2 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/h5").text
            if text2 == "TUC Hierarchy(2000)":
                assert True, f" {text2} ---->  present"
            else:
                assert False, f" {text2} ----> Not Found , Test Failed"
        else:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}-->  found")


@then(u'input SMPP ID')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").send_keys("10001")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('SMPP ID')


@then(u'click on search and check if data is present SMPP ID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/h5").text
            if text1 == "SMPP Info":
                time.sleep(2)
                rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div[1]/table/tbody/tr")
                x = len(rows) - 1
                assert True, f" {x} ----> rows present"
            else:
                assert False, f" No data Present , Test Failed"

            time.sleep(1)
            text2 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/h5").text
            if text2 == "TUC Hierarchy(2000)":
                assert True, f" {text2} ---->  present"
            else:
                assert False, f" {text2} ----> Not Found , Test Failed"
        else:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}-->  found")


@then(u'input API Key')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").send_keys("FUaSvuHl")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('API Key')


@then(u'click on search and check if data is present API Key')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[1]/h5").text
            if text1 == "API Info":
                time.sleep(2)
                rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div[1]/table/tbody/tr")
                x = len(rows) - 1
                assert True, f" {x} ----> rows present"
            else:
                assert False, f" No data Present , Test Failed"

            time.sleep(1)
            text2 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/h5").text
            if text2 == "TUC Hierarchy(2000)":
                assert True, f" {text2} ---->  present"
            else:
                assert False, f" {text2} ----> Not Found , Test Failed"
        else:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}-->  found")


@then(u'input Tuc ID')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").send_keys("2000")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('Tuc ID')


@then(u'click on search and check if data is present Tuc ID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/h5").text
            if text1 == "TUC Hierarchy(2000)":
                time.sleep(2)
                rows = context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/div[1]/table/tbody/tr")
                x = len(rows) - 1
                assert True, f" {x} ----> rows present"
            else:
                assert False, f" {x} ---> rows Present , Test Failed"


@then(u'input User ID')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").clear()
    time.sleep(1)
    context.driver.find_element(By.ID, "enter_type").send_keys("13")
    # select by visible text from dropdown
    time.sleep(1)
    select = Select(context.driver.find_element_by_id('select_type'))
    select.select_by_visible_text('User ID')


@then(u'click on search and check if data is present User ID')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("search_type")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in User_Mgmt_searchObj.User_Mgmt_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text != User_Mgmt_searchObj.User_Mgmt_search_list[x]:
            print(f"{User_Mgmt_searchObj.User_Mgmt_search_list[x]}--> Not found")
            time.sleep(1)
            text1 = context.driver.find_element(By.XPATH,
                                                "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[1]/th[1]").text
            if text1 == "User Name":
                time.sleep(2)
                assert True, f" {text1} ---->  present"
            else:
                assert False, f" {text1} ----> not Present , Test Failed"

            text2 = context.driver.find_element(By.XPATH,
                                                "//*[@id='pills-campaign']/div[2]/div/table/tbody/tr[2]/td[1]").text
            if text2 == "ICICIAdmin":
                time.sleep(2)
                assert True, f" {text2} ---->  present"
            else:
                assert False, f" {text2} ----> not Present , Test Failed"

    # time.sleep(4)
    # context.driver.close()
