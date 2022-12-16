import csv
import time
from behave import *
from selenium.webdriver.common.by import By


@then(u'Click on Download Pop-up')
def step_impl(context):
    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(1)
    button2 = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button2)
    time.sleep(1)
    button = context.driver.find_element(By.ID, "Download")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Download Template and verify file is empty or not')
def step_impl(context):
    time.sleep(5)
    path = "/home/ronit/Downloads/"
    with_ext = "1668664751889_templates.csv"

    file_name = path + with_ext
    with open(file_name, 'r') as obj:
        data = csv.reader(obj)
        for row in data:
            print(row)
            if row:
                assert True, f"{row}"
            else:
                assert False, f"{row}"
