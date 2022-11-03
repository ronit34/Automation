import new_quick_sms_input
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU


@then(u'click on search then click on sent_sms')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "menu_report")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[30]/td[12]/a")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on search in MIS')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click the Download Button in MIS Report')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)



@then(u'select Download file type')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on okay in pop up')
def step_impl(context):
    time.sleep(1)
    # button = context.driver.find_element(By.XPATH, "//*[@id='pills-daily-summary']/div[3]/div/div/div/div[3]/a")
    button = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button)

# @then(u'click on download data')
# def step_impl(context):
#     time.sleep(1)
#     button = context.driver.find_element(By.ID, "pills-download-data-tab")
#     context.driver.execute_script("arguments[0].click();", button)


@then(u'click on download icon')
def step_impl(context):
    time.sleep(4)
    button = context.driver.find_element(By.ID, "pills-download-data-tab")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='report_download']/img")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(2)
    # context.driver.close()
