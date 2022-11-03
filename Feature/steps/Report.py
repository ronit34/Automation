from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
ReportObj = CU.Report()


@then(u'check report is present')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID, "menu_report").is_displayed()


@then(u'click on report')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "menu_report").click()


@then(u'check ALL report elements are present')
def step_impl(context):
    for x in ReportObj.Report_list:
        try:
            status = context.driver.find_element(By.ID, x).is_displayed()
            print(f"{x} --> is {status} ")
        except NameError:
            print(NameError)

@then(u'check ALL report Labels are present')
def step_impl(context):
    for x in ReportObj.Report_list:
        context.driver.implicitly_wait(20)
        if context.driver.find_element(By.ID, x).text == ReportObj.Report_list[x]:
            print(f"{ReportObj.Report_list[x]}--> found")
        else:
            print(f"{ReportObj.Report_list[x]}--> Not found")

    # time.sleep(1)
    # context.driver.close()
