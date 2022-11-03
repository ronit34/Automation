from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time



@then(u'check the campaign is executed or not')
def step_impl(context):
    time.sleep(2)
    for td in context.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/div/table/tbody"):
        if '098765' not in td.text:
            time.sleep(2)
            print(f"campaign executed")
            print(f"campaign executed")
        else:
            assert False , f" campaign not executed "
