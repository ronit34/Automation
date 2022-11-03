import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@then(u'click on ICICIAdmin after which drop down menu will appear')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("dropdown-caret")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'now click on the my account option of the drop down menu')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("user-account")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if User Settings text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/p[1]").text

    if text == "User Settings":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Profile Details text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/p").text

    if text == "Profile Details":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if First Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/div[1]/div/div[1]/label").text

    if text == "First Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Last Name text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/div[1]/div/div[2]/label").text

    if text == "Last Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Company text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/div[1]/div/div[3]/label").text

    if text == "Company":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Email text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/div[1]/div/div[4]/label").text

    if text == "Email":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Phone No text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-account']/div/div[1]/div/div[5]/label").text

    if text == "Phone No":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Save Changes text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='save-changes']").get_attribute('value')

    if text == "Save Changes":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on alert tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("alertsTab")
    context.driver.execute_script("arguments[0].click();", button)

# @then(u'check if SMS Report Alerts text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/p").text
#
#     if text == "SMS Report Alerts":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Daily Usage text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[1]/div[1]/div/p[1]").text
#
#     if text == "Daily Usage":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Weekly Usage text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[1]/div[2]/div/p[1]").text
#
#     if text == "Weekly Usage":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Monthly Day-wise Usage text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[1]/div[3]/div/p[1]").text
#
#     if text == "Monthly Day-wise Usage":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Credit Alerts text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[1]/p").text
#
#     if text == "Credit Alerts":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Low Balance alert by SMS text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[2]/div[1]/div/p[1]").text
#
#     if text == "Low Balance alert by SMS":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Low Balance alert by Email text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[2]/div[2]/div/p[1]").text
#
#     if text == "Low Balance alert by Email":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check if Low Credit alert by Email text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div/div/div/p[1]").text

    if text == "Low Credit alert by Email":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check if Weekly Transaction Report text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[2]/div[3]/div/p[1]").text
#
#     if text == "Weekly Transaction Report":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"
#
# @then(u'check if Monthly Transaction Report text is present or not')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element_by_xpath("//*[@id='pills-alerts']/div/div[2]/div[4]/div/p[1]").text
#
#     if text == "Monthly Transaction Report":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'click on change password tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("changePasswordTab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if Current Password text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-change-number']/div/div[1]/div/div/label[1]").text

    if text == "Current Password":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if New Password text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-change-number']/div/div[1]/div/div/label[2]").text

    if text == "New Password":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Re-enter Password text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='pills-change-number']/div/div[1]/div/div/label[3]").text

    if text == "Re-enter Password":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Submit Request text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='change-num-email']").get_attribute('value')

    if text == "Change Password":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Login History tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[4]/a")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check if IP Address text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr[1]/th[1]").text

    if text == "IP Address":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Login Time text is present or not')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element_by_xpath("//*[@id='campaign-table']/tbody/tr[1]/th[2]").text

    if text == "Login Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()