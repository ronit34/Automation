from behave import *
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import CommonUtility as CU

# ***************************************Quick SMS For English Short*******************


new_multiple_quick_sms_inputObj = CU.new_multiple_quick_sms_input()

# ***************************************Quick SMS For English Long*******************

# import datetime
#
# current_time = datetime.datetime.now()
#
# from datetime import datetime,date
# now = datetime.now()

# import datetime
#
# current_time = datetime.datetime.now()
# from datetime import datetime
# now = datetime.now()
# a = ()

@then(u'create multiple quick sms')
def quick_sms(context):
    # i = 1
    #
    # while (i <= 100):
    #
    #     time.sleep(60)
        # minutes = str(current_time.minute + 2)
        context.driver.find_element(By.ID, "newSms").click()
        # ***************************************Quick SMS For English Short*******************
        if(context.driver.find_element(By.ID, "quick_sms_page_link").is_displayed()):

            #click on quick sms button
            button = context.driver.find_element(By.ID, "quick_sms_page_link")
            context.driver.execute_script("arguments[0].click();", button)

            #inserting data into quick sms field
            for element_id in new_multiple_quick_sms_inputObj.new_multiple_quick_sms_input.keys():
                context.driver.find_element(By.ID, element_id).send_keys(
                    new_multiple_quick_sms_inputObj.new_multiple_quick_sms_input[element_id])
                print(f"{element_id}")

            #click on Insert Template template_name
            time.sleep(1)
            button = context.driver.find_element(By.ID, "insert_template")
            context.driver.execute_script("arguments[0].click();", button)

            #Select Template Type
            button = context.driver.find_element(By.ID, "template_type_id")
            context.driver.execute_script("arguments[0].click();", button)
            select = Select(button)
            select.select_by_value("serv_imp")

            #select template as English short
            time.sleep(1)
            button = context.driver.find_element(By.ID, "template_name")
            context.driver.execute_script("arguments[0].click();", button)
            select = Select(button)
            select.select_by_visible_text("English Long")

            time.sleep(2)
            button = context.driver.find_element(By.ID, "insert_template_to_msg")
            context.driver.execute_script("arguments[0].click();", button)

            time.sleep(1)
            button = context.driver.find_element(By.ID, "send")
            context.driver.execute_script("arguments[0].click();", button)

            # click on multipart SMS
            time.sleep(5)
            multipart= context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/p").text
            if multipart=="Message too long, Select Multipart !!!":
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
                print(f"Message is short no required for multipart")

                # Schedule SMS


            # schedule = context.driver.find_element(By.NAME, "schedule_check")
            # context.driver.execute_script("arguments[0].click();", schedule)
            #
            #
            # # Returns the current local date
            # today = date.today()
            # d1 = today.strftime("%d/%m/%Y")
            # # print(d1)
            # # print(d1)
            # time.sleep(1)
            # dat = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/input")
            # dat.send_keys(d1)
            # dat.send_keys(Keys.TAB)
            # dat.send_keys(now.strftime("%H"))
            # # dat.send_keys(Keys.TAB)
            # # dat.send_keys(a+1)
            #
            # dat.send_keys(current_time.minute + 3)
            #
            # # dat.send_keys(Keys.TAB)
            # # t=str(timedelta(minutes=1))
            # # dat.send_keys(t)
            # #
            #click on send button
            time.sleep(2)
            button = context.driver.find_element(By.ID, "confirm_send_sms")
            context.driver.execute_script("arguments[0].click();", button)

            time.sleep(2)
            button = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/a")
            context.driver.execute_script("arguments[0].click();", button)
        # i=i+1

@then(u'close quick sms')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
