from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU

Type1obj = CU.Type1()
Type2obj = CU.Type2()
Type3obj = CU.Type3()
Type4obj = CU.Type4()
Type5obj = CU.Type5()
Type6obj = CU.Type6()

@then(u'Click on option')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='menu_option']/p")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click on type')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "option_type").click()

@then(u'Click on add type')
def step_impl(context):
    button = context.driver.find_element(By.ID, "add_type")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'Click multiple type')
def step_impl(context):
    for element_id in Type1obj.Type1_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type1obj.Type1_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add_option").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "add_type").click()

    for element_id in Type2obj.Type2_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type2obj.Type2_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add_option").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "add_type").click()

    for element_id in Type3obj.Type3_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type3obj.Type3_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add_option").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "add_type").click()

    for element_id in Type4obj.Type4_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type4obj.Type4_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add_option").click()
    time.sleep(1)
    context.driver.find_element(By.ID, "add_type").click()

    for element_id in Type5obj.Type5_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type5obj.Type5_inputbox_list[element_id])
        print(f"{element_id}")

    context.driver.find_element(By.ID, "add_option").click()
    time.sleep(3)
    context.driver.find_element(By.ID, "add_type").click()

    for element_id in Type6obj.Type6_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            Type6obj.Type6_inputbox_list[element_id])
        print(f"{element_id}")
    time.sleep(3)
    context.driver.find_element(By.ID, "add_option").click()



    # time.sleep(1)
    # context.driver.close()

