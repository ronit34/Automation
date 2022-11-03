import time
from behave import *
import tuc_info_id_list_file
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

import CommonUtility as CU
tuc_hdfcobj = CU.tuc_hdfc()

@then(u'HDFC insert elements')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "smpps").clear()

    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    time.sleep(1)
    button = context.driver.find_element_by_name("onex_gateway")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for element_id in tuc_hdfcobj.tuc_hdfc_list.keys():
        try:
            if element_id != "cancel" and element_id != "onex_gatewaypanel1" and element_id != "save_tuc" and element_id != "cost_unit" and element_id != "accmgr" and element_id != "billing_type" and element_id != "dlt_charges" and element_id != "sms_charges":
                context.driver.find_element(By.ID, element_id).send_keys(tuc_hdfcobj.tuc_hdfc_list[element_id])

            elif element_id == "otp_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "trans_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "promo_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "gov_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "sim_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "default_acc_type":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("On Delivery")

            elif element_id == "cost_unit":
                cu=context.driver.find_element(By.ID, element_id)
                select = Select(cu)
                select.select_by_visible_text("Paisa")

            elif element_id == "accmgr":
                accmgr = context.driver.find_element(By.ID, element_id)
                select = Select(accmgr)

                select.select_by_value("12")

            elif element_id == "billing_type":
                billing_type = context.driver.find_element(By.ID, element_id)
                select = Select(billing_type)
                select.select_by_visible_text("POSTPAID")

            elif element_id == "dlt_charges":
                dlt_charges = context.driver.find_element(By.ID, element_id)
                select = Select(dlt_charges)
                select.select_by_visible_text("On Delivery")

            elif element_id == "sms_charges":
                sms_charges = context.driver.find_element(By.ID, element_id)
                select = Select(sms_charges)
                select.select_by_visible_text("On Delivery")

            elif element_id == "mask_phone":
                mask_phone = context.driver.find_element(By.ID, element_id)
                select = Select(mask_phone)
                select.select_by_visible_text("Yes")

            # else:
            #     time.sleep(1)
            #     button = context.driver.find_element_by_name("onex_gateway")
            #     context.driver.execute_script("arguments[0].click();", button)
            #     # time 3 for firefox
            #     # time.sleep(1)
            #     # button = context.driver.find_element_by_id("save_tuc")
            #     # context.driver.execute_script("arguments[0].click();", button)

        except NameError:
            print(NameError)

    time.sleep(1)
    button = context.driver.find_element_by_id("save_tuc")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    tuc=context.driver.find_element(By.XPATH,"// *[ @ id = 'pills-campaign'] / div[2] / table / tbody / tr[3] / td[1]").text
    if tuc=="HDFC(2001)":
        assert True, f"{tuc} found"
    else:
        assert False, f"{tuc} not found"

    # time.sleep(1)
    # context.driver.close()
