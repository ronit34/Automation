import time

from behave import *
from selenium.webdriver.common.by import By


@then(u'verify the Available Credits in Credits tab')
def step_impl(context):
    time.sleep(2)
    Availabe_Credit_tuc = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr[2]/td[3]").text

    ########### CLICK ON CREDITS ##################
    time.sleep(2)
    button = context.driver.find_element(By.ID, "menu_credit_allocation")
    context.driver.execute_script("arguments[0].click();", button)

    ############# FILL THE Tenant NAME ###############

    time.sleep(2)
    context.driver.find_element(By.ID, "searchTuc").send_keys("ICICI")

    ############# CLICK ON SEARCH ######################
    time.sleep(2)
    button = context.driver.find_element(By.ID, "usr-alloc-search")
    context.driver.execute_script("arguments[0].click();", button)
    #
    time.sleep(2)
    Amount = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr[2]/td[3]").text
    a = int(Amount.replace(',', ''))
    ac = int(Availabe_Credit_tuc.replace(',', ''))
    if (ac == a):
        print(f"Balance is verified and the amount is  = {Amount}")
        assert True
    else:
        assert False, f" test failed "

    # time.sleep(2)
    # context.driver.close()

