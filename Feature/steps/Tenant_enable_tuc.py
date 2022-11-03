from behave import *
import time
from selenium.webdriver.common.by import By

@then(u'check if action button is present on the page for TUC')
def action_present(context):
    time.sleep(1)
    action = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[3]/td[6]/a[3]/div/label/input").is_displayed()

    if action:
        assert True, f"action button found"
    else:
        assert False, f"action button not found"

@then(u'Enable TUC')
def action_present(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[3]/td[6]/a[3]/div/label/input")
    context.driver.execute_script("arguments[0].click();", button)

    # time.sleep(1)
    # context.driver.close()
