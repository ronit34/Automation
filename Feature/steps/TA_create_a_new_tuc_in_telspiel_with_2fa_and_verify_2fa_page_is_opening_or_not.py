import time
from behave import *
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

import CommonUtility as CU

tucinfoidobj = CU.tucinfo_of_telspiel()


@then(u'Click on Add TUC in telspiel with 2fa adn create')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_tuc")
    context.driver.execute_script("arguments[0].click();", button)

    for element_id in tucinfoidobj.tucinfo_id_of_telspiel_list.keys():
        try:
            status = context.driver.find_element(By.ID, element_id).is_displayed()
            print(f"{element_id} --> is {status} ")
        except NameError:
            print(NameError)

    time.sleep(1)
    context.driver.find_element(By.ID, "smpps").clear()

    time.sleep(1)
    context.driver.find_element(By.ID, "smsapi").clear()

    time.sleep(1)
    button = context.driver.find_element(By.NAME, "onex_gateway")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    for element_id in tucinfoidobj.tucinfo_id_of_telspiel_list.keys():

        if element_id != "cancel" and element_id != "onex_gatewaypanel1" and element_id != "save_tuc" and element_id != "billing_type":
            context.driver.find_element(By.ID, element_id).send_keys(
                tucinfoidobj.tucinfo_id_of_telspiel_list[element_id])

        elif element_id == "otp_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "trans_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "promo_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "gov_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "sim_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "default_acc_type":
            cu = context.driver.find_element(By.ID, element_id)
            select = Select(cu)
            select.select_by_visible_text("On Delivery")

        elif element_id == "billing_type":
            billing_type = context.driver.find_element(By.ID, element_id)
            select = Select(billing_type)
            select.select_by_visible_text("PREPAID")

        elif element_id == "validity":
            billing_type = context.driver.find_element(By.ID, element_id)
            select = Select(billing_type)
            select.select_by_visible_text("10")

        elif element_id == "mask_phone":
            mask_phone = context.driver.find_element(By.ID, element_id)
            select = Select(mask_phone)
            select.select_by_visible_text("Yes")

    check_2fa = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div["
                                                      "1]/div[25]/div/div/div/label/input")
    context.driver.execute_script("arguments[0].click();", check_2fa)
    # check_gateway = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div["
    #                                                       "2]/div/div[1]/div[28]/div[1]/label/input")
    # context.driver.execute_script("arguments[0].click();", check_gateway)

    create_btn = context.driver.find_element(By.ID, "save_tuc")
    context.driver.execute_script("arguments[0].click();", create_btn)


@then(u'Click on Add User and create user')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "user_view")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    button1 = context.driver.find_element(By.ID, "create_user")
    context.driver.execute_script("arguments[0].click();", button1)
    time.sleep(2)
    context.driver.find_element(By.ID, "username").send_keys("telsronit")
    context.driver.find_element(By.ID, "password").send_keys("telsronit")
    context.driver.find_element(By.ID, "fname").send_keys("Ronit")
    context.driver.find_element(By.ID, "lname").send_keys("Patel")
    context.driver.find_element(By.ID, "email").send_keys("ronit.patel@onextel.tech")
    context.driver.find_element(By.ID, "mob_no").send_keys("7008427274")
    context.driver.find_element(By.ID, "comp_name").send_keys("ONEXTEL")
    context.driver.find_element(By.ID, "web").send_keys("onextel.com")
    context.driver.find_element(By.ID, "other_mob_no").send_keys("7008427274")
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "role_type"))
    select.select_by_visible_text("TUC Admin")
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "tuc"))
    select.select_by_visible_text("TESTRKP(2003)")

    button2 = context.driver.find_element(By.ID, "save_user")
    context.driver.execute_script("arguments[0].click();", button2)


@then(u'Click User Profile and logout')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//*[@id='profile']/div/p[1]")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(2)
    button2 = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button2)


@then(u'Verify 2fa page is opening or not')
def step_impl(context):
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/label").text
    if txt == "Enter OTP":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"