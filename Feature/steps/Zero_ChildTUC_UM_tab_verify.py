import time
from behave import *
from selenium.webdriver.common.by import By

@then(u'Check User Mgmt tab is present or not')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[@id='menu-sidebar']/div[1]").text
    # print(f"{text}")

    lst = []                      #### Empty List
    lst.append(text)              ####### Appending left menu into list
    # print(f"{lst}")
    # print(f"{lst}")

    new_lst = [i.split('\n') for i in lst]   ##### Splitting list into separate tabs
    print(f"{new_lst}")
    print(f"{new_lst}")

    for i in new_lst:
        # print(i)
        # print(i)
        for j in i:
            if j != "User Management":
               assert True, "User Management Tab is NOT PRESENT"
            else:
                assert False, "User Management Tab is PRESENT"









