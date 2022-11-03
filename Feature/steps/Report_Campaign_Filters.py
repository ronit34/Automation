from selenium.webdriver.support.select import Select
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
Report_quick_searchObj = CU.Report_quick_search()


# @then(u'Enter TUC Name to search')
# def step_impl(context):
#     time.sleep(2)
#     context.driver.find_element_by_id("tuc-report").send_keys("HDFC")
#
#     # time.sleep(3)
#     # # select = Select(context.driver.find_element_by_xpath("ui-id-3"))
#     # # select.select_by_visible_text('HDFC')
#     #
#     entity = context.driver.find_element(By.ID, "ui-id-3")
#     select = Select(entity)
#     select.selectByPartOfVisibleText("HDFC")
#
#     # time.sleep(1)
#     context.driver.find_element_by_id("search").click()