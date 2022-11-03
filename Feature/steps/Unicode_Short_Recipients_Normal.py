from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

import CommonUtility as CU
new_unicode_sms_inputObj = CU.new_quick_sms_input3()

@then(u'insert data into Unicode sms Recipients')
def step_impl(context):
    for element_id in new_unicode_sms_inputObj.new_quick_sms_input3_list.keys():
        context.driver.find_element(By.ID, element_id).send_keys(
            new_unicode_sms_inputObj.new_quick_sms_input3_list[element_id])
        print(f"{element_id}")

    # click on Insert Template template_name
    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template")
    context.driver.execute_script("arguments[0].click();", button)

    # Select Template Type
    button = context.driver.find_element(By.ID, "template_type_id")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_value("serv_imp")

    # select template as English short
    time.sleep(1)
    button = context.driver.find_element(By.ID, "template_name")
    context.driver.execute_script("arguments[0].click();", button)
    select = Select(button)
    select.select_by_visible_text("Hindi Short")

    time.sleep(1)
    button = context.driver.find_element(By.ID, "insert_template_to_msg")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on send now button "{verify}"')
def step_impl(context, verify):
    time.sleep(3)
    creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    # credits = int(creds)
    credits = int(creds.replace(',', ''))
    # click on multipart SMS

    time.sleep(2)
    button = context.driver.find_element(By.ID, "send")
    context.driver.execute_script("arguments[0].click();", button)


    time.sleep(3)
    unicode = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text
    if unicode == "Message Contains Unicode Characters, Please select Allow Unicode to Send this Message!!!":
        time.sleep(1)
        button = context.driver.find_element(By.ID, "ok_modal")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = context.driver.find_element(By.NAME, "unicode_check")
        context.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = context.driver.find_element(By.ID, "send")
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, f"{unicode}"

    time.sleep(3)
    try:
        if (context.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text == "Message too long, Select Multipart !!!"):
            time.sleep(1)
            button = context.driver.find_element(By.ID, "ok_modal")
            context.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            button = context.driver.find_element(By.NAME, "multipart_check")
            context.driver.execute_script("arguments[0].click();", button)
            time.sleep(1)
            button = context.driver.find_element(By.ID, "send")
            context.driver.execute_script("arguments[0].click();", button)
        else:
            print(f"Message is short no required for multipart")
    except NoSuchElementException:
        print(f"Message is short no required for multipart")

    time.sleep(3)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button = context.driver.find_element(By.ID, "confirm_send_sms")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    creds_new = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    # updated_creds = int(creds_new)
    updated_creds = int(creds_new.replace(',', ''))
    verify_creds = int(verify)
    check = credits - updated_creds

    print(f"Credit before sending sms ---> {credits}")
    print(f"Credit after sending sms ---> {updated_creds}")
    print(f"Difference in Credits ---> {check}")

    if (check == verify_creds):
        print(f"{check} ---> Credit deduction is correct")
        print(f"{check} ---> Credit deduction is correct")
    else:
        assert False, print(f"{check} ---> Credit deduction is wrong")

    # time.sleep(1)
    # context.driver.close()
    ##########################################################################################

    # @then(u'check change in credits after sms is sent "{verify}"')
    # def step_impl(context, verify):
    #     # creds = context.driver.find_element_by_xpath("//*[@id='available_credits']").text
    #     # # credits = int(creds)
    #     # credits = int(creds.replace(',', ''))
    #
    #     time.sleep(2)
    #     button = context.driver.find_element(By.ID, "confirm_send_sms")
    #     context.driver.execute_script("arguments[0].click();", button)
    #
    #     time.sleep(1)
    #     button = context.driver.find_element(By.ID, "confirm_send_sms")
    #     context.driver.execute_script("arguments[0].click();", button)
    #
    #