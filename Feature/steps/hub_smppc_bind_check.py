import time
from behave import *
from selenium.webdriver.common.by import By

import Tenant_CommomUtility as CU
hub_smppc_bindObj = CU.hub_smppc_bind()

@then(u'check bind Button is present')
def step_impl(context):
    context.driver.find_element_by_css_selector("[title*='Bind']").is_displayed()

@then(u'Click on bind Button any of createt SMPPC')
def step_impl(context):
    button = context.driver.find_element_by_css_selector("[title*='Bind']")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check bind is succussful or not')
def step_impl(context):
    time.sleep(2)
    status = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[3]/table/tbody/tr[2]/td[4]").text
    print(f"Number Of Binds Is = {status}")
    print(f"Number Of Binds Is = {status}")

    # time.sleep(1)
    # context.driver.close()
