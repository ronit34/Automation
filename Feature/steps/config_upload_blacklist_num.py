from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

import TUC_CommonUtility as CU
ConfigObj = CU.Config()


@then(u'click on Choose a File')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys(
        "/home/onexadmin/Downloads/fileFormats/csv_files/10.csv")
    time.sleep(1)
    context.driver.switch_to.default_content()

@then(u'select category Blacklist')
def step_impl(context):
    time.sleep(2)
    dd = Select(context.driver.find_element_by_id('black_category'))
    # dd.select_by_value("1367")
    # dd.select_by_value("1383")
    # dd.select_by_value("1385")
    dd.select_by_value("1389")


@then(u'click on Upload button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("upload_all")
    context.driver.execute_script("arguments[0].click();", button)


    # time.sleep(2)
    # context.driver.close()