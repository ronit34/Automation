from behave import *
from selenium.webdriver.common.by import By
import time
import CommonUtility as CU
SMPP_SMPPSObj = CU.SMPP_SMPPS_Edit()

@then(u'click on edit icon in smpp')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//*[@id='pills-campaign']/div[2]/table/tbody/tr[2]/td[5]/a[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'change the values in fields')
def step_impl(context):
    time.sleep(2)
    for element_id in SMPP_SMPPSObj.SMPP_SMPPS_Edit_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id) .clear()

    time.sleep(2)
    for element_id in SMPP_SMPPSObj.SMPP_SMPPS_Edit_inputbox_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            SMPP_SMPPSObj.SMPP_SMPPS_Edit_inputbox_list[element_id])
        print(f"{element_id}")

    time.sleep(2)
    context.driver.find_element(By.ID, 'accounttype').send_keys("OTPOTP")
    time.sleep(1)
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")





@then(u'check DND_Filter is deselected or not')
def step_impl(context):
    time.sleep(2)
    checkbox = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[20]/div/div/div[1]/label/label/input").is_selected()
    if checkbox == False:
        assert True
    else:
        assert False, f"checkbox is not selected"


@then(u'click on update button in SMPPS')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_smpps")
    context.driver.execute_script("arguments[0].click();", button)




@then(u'check SMPP is edited or not')
def step_impl(context):
    time.sleep(2)
    checkbox = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[1]").text
    if checkbox == "Edited":
        assert True
    else:
        assert False, f"SMPP is not updated"