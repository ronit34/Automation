from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

import TUC_CommonUtility as CU
ConfigObj = CU.Config()

@then(u'click on Choose a File for whitelist upload')
def step_impl(context):
    time.sleep(1)
    a = context.driver.switch_to.frame("up_onex_file")
    context.driver.find_element_by_id("file1").send_keys(
        "/home/onexadmin/Downloads/fileFormats/xlxs_files/10.xlsx")
    time.sleep(1)
    context.driver.switch_to.default_content()

@then(u'select category Whitelist')
def step_impl(context):
    time.sleep(2)
    dd = Select(context.driver.find_element_by_id('whitelist_category'))
    # dd.select_by_value("1368")
    # dd.select_by_value("1384")
    # dd.select_by_value("1386")
    dd.select_by_value("1390")