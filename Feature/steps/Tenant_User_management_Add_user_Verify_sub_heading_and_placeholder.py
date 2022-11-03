from behave import *
from selenium.webdriver.common.by import By
import time


@then(u'Click on Add_User')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, "create_user")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'Verify Sub-heading and Placeholder_add_user')
def step_impl(context):
    sub_head_txt = context.driver.find_element(By.ID, "current_date").text
    # print(sub_head_txt)
    if sub_head_txt == "Tuesday 11 October 2022":
        assert True, f"{sub_head_txt}"
    else:
        assert False, f"{sub_head_txt}"

    username = context.driver.find_element(By.ID, "username").get_attribute('placeholder')
    print(username)
    if username == "Name":
        assert True, f"{username}"
    else:
        assert False, f"{username}"

    password = context.driver.find_element(By.ID, "password").get_attribute('placeholder')
    print(password)
    if password == "Enter Password":
        assert True, f"{password}"
    else:
        assert False, f"{password}"

    fname = context.driver.find_element(By.ID, "fname").get_attribute('placeholder')
    print(fname)
    if fname == "First Name":
        assert True, f"{fname}"
    else:
        assert False, f"{fname}"

    lname = context.driver.find_element(By.ID, "lname").get_attribute('placeholder')
    print(lname)
    if lname == "Last Name":
        assert True, f"{lname}"
    else:
        assert False, f"{lname}"

    email = context.driver.find_element(By.ID, "email").get_attribute('placeholder')
    print(email)
    if email == "User Email ID":
        assert True, f"{email}"
    else:
        assert False, f"{email}"

    phone_number = context.driver.find_element(By.ID, "mob_no").get_attribute('placeholder')
    print(phone_number)
    if phone_number == "0000000000":
        assert True, f"{phone_number}"
    else:
        assert False, f"{phone_number}"

    company_name = context.driver.find_element(By.ID, "comp_name").get_attribute('placeholder')
    print(company_name)
    if company_name == "Company Name":
        assert True, f"{company_name}"
    else:
        assert False, f"{company_name}"

    web = context.driver.find_element(By.ID, "web").get_attribute('placeholder')
    print(web)
    if web == "Enter Web URL":
        assert True, f"{web}"
    else:
        assert False, f"{web}"

    mobile_number = context.driver.find_element(By.ID, "other_mob_no").get_attribute('placeholder')
    print(mobile_number)
    if mobile_number == "0000000000":
        assert True, f"{mobile_number}"
    else:
        assert False, f"{mobile_number}"
