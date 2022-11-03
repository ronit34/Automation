from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'click on delete icon in SMPP')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[5]/a[2]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on delete button to confirm delete')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check SMPP is deleted or not')
def step_impl(context):
    time.sleep(2)
    for td in context.driver.find_elements_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tbody/td/tr"):
        if 'Edited' in td.text:
            assert True
        else:
            assert False, f"SMPP is not deleted"