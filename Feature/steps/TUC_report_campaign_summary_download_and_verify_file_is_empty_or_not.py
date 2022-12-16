import csv
import time
from behave import *
from selenium.webdriver.common.by import By
from zipfile import ZipFile


@then(u'Click on Campaign Summary')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-campaign-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Search in campaign summary')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Download in csv file')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button1 = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button1)


@then(u'Click on Download csv file pop-up')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Click on Download Data for campaign summary file check')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-download-data-tab")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "pills-download-data-tab")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(2)
    button2 = context.driver.find_element(By.ID, "pills-download-data-tab")
    context.driver.execute_script("arguments[0].click();", button2)


@then(u'Click on Download button in download data')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='report_download']/img")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button1 = context.driver.find_element(By.XPATH, "//*[@id='report_download']/img")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(1)
    button2 = context.driver.find_element(By.XPATH, "//*[@id='report_download']/img")
    context.driver.execute_script("arguments[0].click();", button2)
    time.sleep(1)
    button3 = context.driver.find_element(By.XPATH, "//*[@id='report_download']/img")
    context.driver.execute_script("arguments[0].click();", button3)


@then(u'Open downloaded file and verify empty or not')
def step_impl(context):
    time.sleep(2)
    file_name = context.driver.find_element(By.XPATH, "//*[@id='campaign-summary-table']/tbody/tr[2]/td[4]").text
    time.sleep(5)
    download_file_path = '/home/ronit/Downloads/'
    file_path = download_file_path + file_name
    time.sleep(2)
    with ZipFile(file_path, 'r') as obj:
        obj.extractall(path=download_file_path)

    split_ext = file_name.split('.', 1)
    extension = '.csv'
    file_path_name_with_ext = split_ext[0]
    print(file_path_name_with_ext)

    csv_file = file_path_name_with_ext[:-14]
    print(csv_file)
    path_ = download_file_path + csv_file + extension
    print(path_)
    time.sleep(5)
    with open(path_, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
            if row == 0:
                assert False, f"{row} -- File is empty"
            else:
                assert True, f"{row} -- File is not empty"


@then(u'Close Windows Driver')
def step_impl(context):
    time.sleep(2)
    context.driver.close()
