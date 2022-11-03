from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU


@then(u'click on the total counts')
def step_impl(context):
    time.sleep(2)
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[32]/th[26]/a")
    # button = context.driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr[33]/th[26]/a")
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[33]/th[26]/a")
    context.driver.execute_script("arguments[0].click();", button)



@then(u'copy UUID and paste in search tab and verify porterid text')
def step_impl(context):
    time.sleep(2)
    UUID = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[3]").text
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element_by_id("uuid").send_keys(UUID)
    time.sleep(1)
    button = context.driver.find_element_by_id("search")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element_by_id("uuid_panel").click()

    TelcoID = context.driver.find_element_by_xpath("//*[@id='hover_uuid']/p[1]").text
    PorterID = context.driver.find_element_by_xpath("//*[@id='hover_uuid']/p[2]").text

    time.sleep(2)
    if TelcoID.startswith('Telco ID :'):
        assert True
    else:
        assert False, print(f"{TelcoID} ---> text mismatch")

    time.sleep(1)
    if PorterID.startswith('Porter ID :'):
        assert True
    else:
        assert False, print(f"{PorterID} ---> text mismatch")

    # print(type(TelcoID))
    # print(type(PorterID))

    time.sleep(2)

