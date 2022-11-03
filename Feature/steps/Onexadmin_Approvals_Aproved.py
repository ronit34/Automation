from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on Approved tab to check status')
def step_impl(context):
    context.driver.find_element(By.ID, "pills-approved-tab").click()
    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div/table/tbody/tr[2]/td[1]").is_displayed()):
            # input("Press Enter.......")
            print(f"Approved Successfully..........")

    # time.sleep(1)
    # context.driver.close()
