import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Enter OTP in special character')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "first").send_keys('@')
    time.sleep(2)
    context.driver.find_element(By.ID, "second").send_keys("$")
    time.sleep(2)
    context.driver.find_element(By.ID, "third").send_keys("%")
    time.sleep(2)
    context.driver.find_element(By.ID, "fourth").send_keys("*")
    time.sleep(2)
    context.driver.find_element(By.ID, "fifth").send_keys("&")
    time.sleep(2)
    context.driver.find_element(By.ID, "sixth").send_keys("@")
    time.sleep(2)


@then(u'Verify character available or not')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[1]").text
    print(txt)
    if txt == '':
        assert True, f"----{txt}-----"
    else:
        assert False, f"----{txt}-----"

    time.sleep(2)
    txt1 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[2]").text
    print(txt1)
    if txt1 == '':
        assert True, f"----{txt1}-----"
    else:
        assert False, f"----{txt1}-----"

    time.sleep(2)
    txt2 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[3]").text
    print(txt2)
    if txt2 == '':
        assert True, f"----{txt2}-----"
    else:
        assert False, f"----{txt2}-----"

    time.sleep(2)
    txt3 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[4]").text
    print(txt3)
    if txt == '':
        assert True, f"----{txt3}-----"
    else:
        assert False, f"----{txt3}-----"

    time.sleep(2)
    txt4 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[5]").text
    print(txt4)
    if txt4 == '':
        assert True, f"----{txt4}-----"
    else:
        assert False, f"----{txt4}-----"

    time.sleep(2)
    txt5 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input[6]").text
    print(txt5)
    if txt5 == '':
        assert True, f"----{txt5}-----"
    else:
        assert False, f"----{txt5}-----"

