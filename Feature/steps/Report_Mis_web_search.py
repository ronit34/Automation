import new_quick_sms_input
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
Report_MIS_quick_searchObj = CU.Report_MIS_quick_search()


@then(u'click on report in left menu')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "menu_report")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on search in MIS tab')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on the number of sms sent')
def step_impl(context):
    time.sleep(2)
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[30]/td[12]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[33]/th[26]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    button = context.driver.find_element(By.XPATH,
            "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[33]/th[26]/a")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on search and check if the data is present')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for x in Report_MIS_quick_searchObj.Report_mis_quick_search_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.XPATH, x).text == Report_MIS_quick_searchObj.Report_mis_quick_search_list[x]:
            print(f"{Report_MIS_quick_searchObj.Report_mis_quick_search_list[x]}--> found")
        else:
            print(f"{Report_MIS_quick_searchObj.Report_mis_quick_search_list[x]}--> Not found")


    # time.sleep(2)
    # context.driver.close()

