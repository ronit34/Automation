from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'click on user management tab')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='menu_users']/p").click()

@then(u'click on tenants tab')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='tenant_view']").click()

@then(u'check if user management text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "User Management":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Super Admin text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='profile']/div/p[1]").text

    if text == "Super Admin":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Platform (1) text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='profile']/div/p[2]").text

    if text == "Platform (1)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Tenant Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[1]/a").text

    if text == "Tenant Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if TeleMarketer ID text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]/a").text

    if text == "TeleMarketer ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]/a").text

    if text == "Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Action text is present or not in user management tab')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[4]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on add tenant button in usermanagement tab')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='create_tenant']").click()

@then(u'check if Tenant Info text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[1]/h5").text

    if text == "Tenant Info":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Tenant Name text inside add tenant is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='namepanel1']").text

    if text == "Tenant Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if TeleMarketer ID text inside add tenant is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='telemaridpanel1']").text

    if text == "TeleMarketer ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Description text inside add tenant is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[6]/div/label").text

    if text == "Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Licenses text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[8]/h5").text

    if text == "Licenses":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Child TUC text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='childtucpanel1']").text

    if text == "Child TUC* (498)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMPPS text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='smppspanel1']").text

    if text == "SMPPS* (500)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if SMS API text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='smsapipanel1']").text

    if text == "SMS API* (600)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Create button text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='save_tenant']").is_displayed()

    if text:
        print("button present")
    else:
        print("button not present")

@then(u'click on cancel button in user management tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("cancel")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'click on User tab')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='user_view']").click()

@then(u'check if  User Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[1]/a").text

    if text == "User Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  First Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[2]/a").text

    if text == "First Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Last Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[3]/a").text

    if text == "Last Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Email text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[4]/a").text

    if text == "Email":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Mobile Number text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[5]/a").text

    if text == "Mobile Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Company Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[6]/a").text

    if text == "Company Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Role Type text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[7]/a").text

    if text == "Role Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Action text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/table/tbody/tr/th[8]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the add user inside the user tab')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element_by_xpath("//*[@id='create_user']").click()

@then(u'check if  Create User text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "Create User":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  User Info text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[2]/div/div[1]/div[1]/h5").text

    if text == "User Info":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  User Name* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='usernamepanel1']").text

    if text == "User Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Password* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='passwordpanel1']").text

    if text == "Password*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  First Name* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='fnamepanel1']").text

    if text == "First Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Last Name* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='lnamepanel1']").text

    if text == "Last Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Email* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='emailpanel1']").text

    if text == "Email*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Mobile Number* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='mob_nopanel1']").text

    if text == "Mobile Number*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Company Name* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='comp_namepanel1']").text

    if text == "Company Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Web* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='webpanel1']").text

    if text == "Web*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Other Mobile Number text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='other_mob_nopanel1']").text

    if text == "Other Mobile Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Role Type* text inside the user tab is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='role_typepanel1']").text

    if text == "Role Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()