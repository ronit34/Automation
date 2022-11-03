from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

@then(u'click on campaign_search option')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "pills-campaign-tab")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on Download button')
def download(context):
    #click on Download button
    time.sleep(2)
    button = context.driver.find_element(By.ID,"dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.ID, "dropdownMenuLink").click()

    #Selecting option for download file
    button = context.driver.find_element(By.ID,"download_csv")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    # context.driver.find_element_by_link_text('Okay').click()
    context.driver.find_element_by_id('okay').click()

@then(u'go to download data section and download the file')
def step_impl(context):
    # click on Download Data tab
    time.sleep(1)
    context.driver.find_element(By.ID, "pills-download-data-tab").click()

    #And check status of the file if completed then download it
    time.sleep(4)
    # context.driver.refresh()
    time.sleep(2)
    status=context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr[2]/td[6]").text
    if(status=="completed"):
        print(f"click on download icon for downloading file")
        time.sleep(5)
        # context.driver.refresh()
        time.sleep(1)
        context.driver.find_element(By.ID, "report_download").click()
    else:
        print(f"Something Went Wrong,Please Check!")
        print(f"Something Went Wrong,Please Check!")

    # time.sleep(1)
    # context.driver.close()


