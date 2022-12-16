import csv
import time
from behave import *
from selenium.webdriver.common.by import By
import zipfile


@then(u'Click on Total Number of MIS')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Enter Wrong Number and Search')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "mobile").send_keys("67475684345")
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Card Count')
def step_impl(context):
    time.sleep(2)
    txt = context.driver.find_element(By.XPATH, "//*[@id='v-pills-tab']/div[1]/p[2]").text
    print(txt)
    if txt == "0":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"


@then(u'Click on Download All')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)
    button1 = context.driver.find_element(By.ID, "download_csv_all")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(1)
    button2 = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button2)


@then(u'Verify file is empty or not')
def step_impl(context):
    time.sleep(5)

    file = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[4]").text
    print()
    path_file = "/home/ronit/Downloads/"
    path = path_file + file
    print(path)
    time.sleep(2)
    with zipfile.ZipFile(path) as zf:
        for file in zf.namelist():
            if not file.endswith('.csv'):
                continue
            with zf.open(file) as fl:
                csvdata = csv.reader(fl)
                for row in csvdata:
                    print(row)
                    if row == "":
                        assert True, f"{row}"
                    else:
                        assert False, f"{row}"


