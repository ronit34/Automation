import re
import new_quick_sms_input
from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU


@then(u'click on the total mis counts')
def step_impl(context):
    time.sleep(2)
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[33]/th[26]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[33]/th[26]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check web count and submitted count')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_id("web_tab").text
    sub = context.driver.find_element_by_xpath("//*[@id='v-pills-tab']/div[1]/p[2]").text
    s1 = re.sub("[^0-9]", "", text)
    time.sleep(1)
    if s1 == sub:
        assert True, "Same values"
    else:
        assert False, f"{text} is not present"

@then(u'Click on okay in the pop up')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button)


