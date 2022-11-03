#********************** Required Import *****************************************
from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on TUC List')
def click_tuc_list(context):
# ********************** clicking on dropdown tuc list *****************************************
    context.driver.find_element(By.ID, "searchTuc").send_keys("Onexmedia")

#********************** Selecting Required Options from TUC Dropdown List ***********************
    # context.driver.find_element(By.XPATH,"  // *[ @ id = 'tuc_list'] / option[2]").click()

@then(u'click on search')
def click_search(context):
# ********************** Click on search button for userwise allocation
    context.driver.find_element(By.ID, "usr-alloc-search").click()

    # time.sleep(1)
    # context.driver.close()

