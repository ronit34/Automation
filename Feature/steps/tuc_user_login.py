from behave import *
from selenium.webdriver.common.by import By

import time

@then(u'Check todays date is present')
def date_present(context):
    context.driver.find_element(By.ID, "current_date").is_displayed()

    # time.sleep(1)
    # context.driver.close()