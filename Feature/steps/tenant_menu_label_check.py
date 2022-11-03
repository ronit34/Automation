from behave import *
from selenium.webdriver.common.by import By
import time

@then(u'check label of Report')
def report(context):
    time.sleep(3)
    report = context.driver.find_element(By.ID, "menu_report").text
    if (report == "Reports"):
        assert True, f"{report} found"
    else:
        assert False, f"{report} not found"

@then(u'check label of tenant Telco Reports')
def report(context):
    time.sleep(3)
    report = context.driver.find_element(By.XPATH, "//*[@id='menu_telco_reports']/p").text
    if (report == "Telco Reports"):
        assert True, f"{report} found"
    else:
        assert False, f"{report} not found"

@then(u'check label of Hub')
def hub(context):
    time.sleep(1)
    hub = context.driver.find_element(By.ID, "menu_hub").text
    if (hub == "HUB"):
        assert True, f"{hub} found"
    else:
        assert False, f"{hub} not found"

@then(u'check label of tenant URL')
def hub(context):
    time.sleep(1)
    url = context.driver.find_element(By.XPATH, "//*[@id='menu_url_tnt']/p").text
    if (url == "URL"):
        assert True, f"{url} found"
    else:
        assert False, f"{url} not found"

# @then(u'check label Approvals')
# def approvals(context):
#     approvals = context.driver.find_element(By.ID, "menu_approvals").text
#     if (approvals == "Approvals"):
#         assert True, f"{approvals} found"
#     else:
#         assert False, f"{approvals} not found"

# @then(u'check label of tenant Spam')
# def approvals(context):
#     spam = context.driver.find_element(By.XPATH, "//*[@id='menu_spam']/p").text
#     if (spam == "Spam"):
#         assert True, f"{spam} found"
#     else:
#         assert False, f"{spam} not found"

@then(u'check label of Test SMS')
def test_sms(context):
    test_sms = context.driver.find_element(By.ID, "menu_test_sms").text
    if (test_sms == "Test SMS"):
        assert True, f"{test_sms} found"
    else:
        assert False, f"{test_sms} not found"

@then(u'check label of Monitor')
def monitor(context):
    monitor = context.driver.find_element(By.XPATH, "//*[@id='menu_mon2']/p").text
    if (monitor == "Mon2"):
        assert True, f"{monitor} found"
    else:
        assert False, f"{monitor} not found"

@then(u'check label of Options are present')
def Options(context):
    Options = context.driver.find_element(By.ID, "menu_option").text
    if (Options == "Options"):
        assert True, f"{Options} found"
    else:
        assert False, f"{Options} not found"

@then(u'check label of tenant Notification')
def Options(context):
    notification = context.driver.find_element(By.XPATH, "//*[@id='menu_notification']/p").text
    if (notification == "Notification"):
        assert True, f"{notification} found"
    else:
        assert False, f"{notification} not found"

    # time.sleep(1)
    # context.driver.close()