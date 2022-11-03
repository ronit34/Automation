from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import CommonUtility as CU

API_dropdown1obj = CU.API_dropdown1()
API_dropdown2obj = CU.API_dropdown2()
API_dropdown3obj = CU.API_dropdown3()
API_dropdown4obj = CU.API_dropdown4()
API_dropdown5obj = CU.API_dropdown5()

@then(u'generate multiple api')
def step_impl(context):
    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]").is_displayed()):
        button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)

        for element_id in API_dropdown1obj.API_dropdown1_inputbox_list.keys():
            try:
                context.driver.implicitly_wait(20)
                element_obj = context.driver.find_element(By.XPATH, element_id)
                context.driver.implicitly_wait(20)
                select = Select(element_obj)
                context.driver.implicitly_wait(20)
                select.select_by_visible_text(
                    API_dropdown1obj.API_dropdown1_inputbox_list[element_id])

            except NameError:
                print(NameError)

        context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()
        time.sleep(1)

    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[3]").is_displayed()):
        button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)

        for element_id in API_dropdown2obj.API_dropdown2_inputbox_list.keys():
            try:
                context.driver.implicitly_wait(20)
                element_obj = context.driver.find_element(By.XPATH, element_id)
                context.driver.implicitly_wait(20)
                select = Select(element_obj)
                context.driver.implicitly_wait(20)
                select.select_by_visible_text(
                    API_dropdown2obj.API_dropdown2_inputbox_list[element_id])

            except NameError:
                print(NameError)

        context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()
        time.sleep(1)

    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[4]").is_displayed()):
        button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)

        for element_id in API_dropdown3obj.API_dropdown3_inputbox_list.keys():
            try:
                context.driver.implicitly_wait(20)
                element_obj = context.driver.find_element(By.XPATH, element_id)
                context.driver.implicitly_wait(20)
                select = Select(element_obj)
                context.driver.implicitly_wait(20)
                select.select_by_visible_text(
                    API_dropdown3obj.API_dropdown3_inputbox_list[element_id])

            except NameError:
                print(NameError)

        context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()
        time.sleep(1)
    #
    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[5]").is_displayed()):
        button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)

        for element_id in API_dropdown4obj.API_dropdown4_inputbox_list.keys():
            try:
                context.driver.implicitly_wait(20)
                element_obj = context.driver.find_element(By.XPATH, element_id)
                context.driver.implicitly_wait(20)
                select = Select(element_obj)
                context.driver.implicitly_wait(20)
                select.select_by_visible_text(
                    API_dropdown4obj.API_dropdown4_inputbox_list[element_id])

            except NameError:
                print(NameError)

        context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()
        time.sleep(1)

    if (context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[6]").is_displayed()):
        button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/a")
        context.driver.execute_script("arguments[0].click();", button)

        for element_id in API_dropdown5obj.API_dropdown5_inputbox_list.keys():
            try:
                context.driver.implicitly_wait(20)
                element_obj = context.driver.find_element(By.XPATH, element_id)
                context.driver.implicitly_wait(20)
                select = Select(element_obj)
                context.driver.implicitly_wait(20)
                select.select_by_visible_text(
                    API_dropdown5obj.API_dropdown5_inputbox_list[element_id])

            except NameError:
                print(NameError)

        context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[3]/a[2]").click()
        time.sleep(1)

    # time.sleep(1)
    # context.driver.close()