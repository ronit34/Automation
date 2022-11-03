from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'Master Balance Match With Available Credit')
def step_impl(context):
    # Checking Available Credits is Zero
    time.sleep(1)
    credit = context.driver.find_element_by_id('available_credits').text
    print(f"Available credit Is = {credit}")

    #Updating Master Balance
    context.driver.find_element(By.ID, "update_balance").click()
    context.driver.find_element(By.ID, "amount").send_keys(10000000)
    time.sleep(1)
    entered_amount = context.driver.find_element(By.ID, 'amount').get_attribute('value')


    # title = context.driver.find_element(By.ID, 'balance_title').click()

    # print(f"Balance Title={title}")
    print(f"Enter amount is = {entered_amount}")

    time.sleep(2)
    context.driver.find_element(By.ID, "add").click()

    time.sleep(2)
    Current_balance=context.driver.find_element_by_id('current_balance').text
    print(f"Current Balance Is = {Current_balance}")

    Updated_Available_credit = context.driver.find_element_by_id('available_credits').text
    print(f"After Updating Master Balance Available credit Is = {Updated_Available_credit}")

    # z=int(float(Current_balance))
    # x=int(Updated_Available_credit)
    if (Current_balance==entered_amount):
        print(f"Entered Amount Is Matched With Current Balance")
        if(Updated_Available_credit==entered_amount):
            print(f"Entered Amount Is Matched With Available Credit")
        elif NameError:
            print(f"Entered Amount 'IS NOT' Matched With Available Credit")
    else:
        print(f"Exit Main If Block Due To Entered Amount 'IS NOT' Matched With Current Balance")

    #Credit Allocation---->Userwise Allocation---->History
    time.sleep(1)
    context.driver.find_element(By.ID, "menu_credit_allocation").click()

    time.sleep(1)                               
    x=context.driver.find_element(By.XPATH, "//*[@id='campaign-table']/tbody/tr[2]/td[3]").text
    print(f"Platform History Amount = {x}")
    if (x == entered_amount):
        print(f"Entered Amount Is Matched With Platform History Amount")
    else:
        print(f"Entered Amount 'IS NOT' Matched With Platform History Amount")


    #Credit Allocation-------->Userwise Allocation---->Update Credit
    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_credit")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    CA = context.driver.find_element_by_id('available_credits').text
    print(f"Credit Allocation----->Update Credit---->Available credit Is = {CA}")
    if (CA == entered_amount):
        print(f"Entered Amount Is Matched With Credit Allocation----->Update Credit---->Available credit")
    else:
        print(f"Entered Amount 'IS NOT' Matched With Credit Allocation----->Update Credit---->Available credit")
    print(context.driver.find_element_by_id("current_date").text)

    # time.sleep(1)
    # context.driver.close()