import new_quick_sms_input
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
Report_quick_searchObj = CU.Report_quick_search()

@then(u'sent sms through qucik')
def step_impl(context):
    context.driver.find_element(By.ID, "newSms").click()

    new_quick_sms_input.quick_sms(context)


    # pass

@then(u'click on report_search option')
def step_impl(context):
    time.sleep(5)
    button = context.driver.find_element(By.ID,"menu_report")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button = context.driver.find_element(By.ID,"pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys(8605493727)
    context.driver.find_element(By.ID, "search").click()

@then(u'Then Check sent sms is in report or not')
def step_impl(context):
    time.sleep(1)
    for x in Report_quick_searchObj.Report_quick_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == Report_quick_searchObj.Report_quick_search_list[x]:
            print(f"{Report_quick_searchObj.Report_quick_search_list[x]}--> found")
        else:
            print(f"{Report_quick_searchObj.Report_quick_search_list[x]}--> Not found")

@then(u'close report quick search')
def step_impl(context):
    time.sleep(1)
    context.driver.close()

