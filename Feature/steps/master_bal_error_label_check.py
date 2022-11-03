import time
import CommonUtility as CU
practise1Obj = CU.practise1()
from behave import *
from selenium.webdriver.common.by import By

@then(u'check iteratively error labels')
def step_impl(context):

    login(context, "onexsa", "onexsa",practise1Obj.amount_list)

def login(context, username, password,amt):
    i=0
    while i<=5:
    #     from selenium import webdriver
    #     from webdriver_manager.chrome import ChromeDriverManager
    #     driver = webdriver.Chrome(ChromeDriverManager().install())
    #     context.driver = driver
        context.driver.get("http://localhost:8000/index")
        context.driver.find_element(By.ID, "email").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys(password)
        context.driver.implicitly_wait(100)
        # check box
        context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").click()
        context.driver.implicitly_wait(100)

        # login button press
        button = context.driver.find_element(By.ID, "login_button")
        context.driver.execute_script("arguments[0].click();", button)

        context.driver.find_element(By.ID, "menu_master_balance").click()

        i=0
        while(i<=5):
            time.sleep(2)
            for x in amt:
                context.driver.find_element(By.ID, "update_balance").click()


            # for x in amt:
                context.driver.find_element(By.ID, "amount").send_keys(x)
                context.driver.find_element(By.ID, "add").click()
                time.sleep(5)
                if (context.driver.find_element(By.XPATH, "//*[@id='myModal']/div/div/div[2]/div[2]/span/span").is_displayed()):
                    context.driver.find_element(By.XPATH, "//*[@id='cancel']").click()
            input("Press")
            i=i+1

                # input("Press Enter...........")


        # if (send_keys==0):
        # for y in practise1Obj.practise1_label_error_list:
        #             try:
        #                 status = context.driver.find_element(By.XPATH, y).is_displayed()
        #                 print(f"{y} --> is {status} ")
        #             except NameError:
        #                 print(NameError)
        #
        # for x in practise1Obj.practise1_label_error_list:
        #             context.driver.implicitly_wait(20)
        #             if context.driver.find_element(By.XPATH, x).text == practise1Obj.practise1_label_error_list[x]:
        #                 print(f"{practise1Obj.practise1_label_error_list[x]}--> found")
        #             else:
        #                 print(f"{practise1Obj.practise1_label_error_list[x]}--> Not found")
        #  # context.driver.find_element(By.XPATH,"// *[ @ id = 'myModal'] / div / div / div[2] / div[2] / span / span").is_displayed()
        #
        #
        # time.sleep(2)






        # print(f"login Number-----------------------------------> {i}")
        # i=i+1
        # time.sleep(1)
        # context.driver.close()


