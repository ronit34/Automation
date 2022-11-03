import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'Click on Add TUC for growtel')
def step_impl(context):
    button = context.driver.find_element(By.ID, "create_tuc")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details for growtel tuc')
def step_impl(context):
    context.driver.find_element(By.ID, "name").send_keys("groww")
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, "otp_acc_type"))
    select.select_by_visible_text("On Delivery")
    select1 = Select(context.driver.find_element(By.ID, "trans_acc_type"))
    select1.select_by_visible_text("On Delivery")
    select2 = Select(context.driver.find_element(By.ID, "promo_acc_type"))
    select2.select_by_visible_text("On Delivery")
    select3 = Select(context.driver.find_element(By.ID, "gov_acc_type"))
    select3.select_by_visible_text("On Delivery")
    select4 = Select(context.driver.find_element(By.ID, "sim_acc_type"))
    select4.select_by_visible_text("On Delivery")
    select5 = Select(context.driver.find_element(By.ID, "default_acc_type"))
    select5.select_by_visible_text("On Delivery")
    select6 = Select(context.driver.find_element(By.ID, "billing_type"))
    select6.select_by_visible_text("PREPAID")
    context.driver.find_element(By.ID, "validity").send_keys("10")
    select7 = Select(context.driver.find_element(By.ID, "mask_phone"))
    select7.select_by_visible_text("Yes")
    button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div["
                                                   "1]/div[25]/div/div/div/label/input")
    context.driver.execute_script("arguments[0].click();", button)

    button1 = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div["
                                                    "1]/div[30]/div[1]/label/input")
    context.driver.execute_script("arguments[0].click();", button1)

    context.driver.find_element(By.ID, "childtuc").send_keys("0")
    context.driver.find_element(By.ID, "smpps").clear()
    context.driver.find_element(By.ID, "smpps").send_keys("1")
    # context.driver.find_element(By.ID, "smsapi").send_keys("1")


@then(u'Click on create growtel for tuc')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_tuc")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Insert details for growtel in tuc user')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "username").send_keys("growronit")
    context.driver.find_element(By.ID, "password").send_keys("growronit")
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
    select.select_by_visible_text("groww(2002)")


@then(u'Click on create growtel for user in tuc')
def step_impl(context):
    button2 = context.driver.find_element(By.ID, "save_user")
    context.driver.execute_script("arguments[0].click();", button2)


@then(u'Verify 2fa page pop-up is opening or not')
def step_impl(context):
    time.sleep(5)
    txt = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/p[2]/span[1]").text
    if txt == "Two-Factor":
        assert True, f"{txt}"
    else:
        assert False, f"{txt}"

    txt1 = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/p[2]/span[2]").text
    if txt1 == "Authentication":
        assert True, f"{txt1}"
    else:
        assert False, f"{txt1}"