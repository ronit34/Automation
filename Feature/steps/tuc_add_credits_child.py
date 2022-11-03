import time

from behave import *
from selenium.webdriver.common.by import By

@then(u'Check the Available Credits')
def step_impl(context):
    time.sleep(1)
    credit = context.driver.find_element_by_id('available_credits').text
    print(f"Available credit Is={credit}")

# @then(u'click on Manage Credit icon')
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[4]/img").click()

    time.sleep(1)
    context.driver.find_element(By.ID, "credits_amount").send_keys("100")

    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='add_credit_div']/label").click()


# @then(u'Click on update to add credits')
    time.sleep(1)
    # context.driver.find_element(By.ID, "delete").click()
    context.driver.find_element(By.ID, "update_credits").click()

# @then(u'check Updated credit')
    time.sleep(5)
    Updated_Available_credit = context.driver.find_element_by_id('available_credits').text
    print(f"Updated Available credit Is={Updated_Available_credit}")
    z = int(credit.replace(',', ''))
    x = int(Updated_Available_credit.replace(',', ''))
    p = int(z - x)

    if (p==100):
        print(f"Balance is deducted and Updated Available Credit Is = {Updated_Available_credit}")
        assert True
    else:
        assert False, f" not credited as per cost"

    # time.sleep(1)
    # context.driver.close()
