from behave import *
from selenium.webdriver.common.by import By
import time
@then(u'check label Campaign')
def camp(context):
    camp = context.driver.find_element(By.ID, "menu_campaigns").text
    if camp == "Campaign":
        assert True, f"{camp} found"
    else:
        assert False, f"{camp} not found"

@then(u'check label of TUC Telco Reports')
def camp(context):
    telco = context.driver.find_element(By.XPATH, "//*[@id='menu_telco_reports']/p").text
    if telco == "Telco Reports":
        assert True, f"{camp} found"
    else:
        assert False, f"{camp} not found"

@then(u'check label of DLT')
def dlt(context):
    dlt = context.driver.find_element(By.ID, "menu_manage").text
    if dlt == "DLT":
        assert True, print(f"{dlt} found")
    else:
        assert False, f"{dlt} not found"

@then(u'check label of SMPP')
def smpp(context):
    smpp = context.driver.find_element(By.ID, "menu_smpps_view").text
    if smpp == "SMPP":
        assert True, print(f"{smpp} found")
    else:
        assert False, f"{smpp} not found"

@then(u'check label of API')
def api(context):
    api = context.driver.find_element(By.ID, "menu_api").text
    if api == "API":
        assert True, f"{api} found"
    else:
        assert False, f"{api} not found"

@then(u'check label of Phonebook')
def phone(context):
    phone = context.driver.find_element(By.ID, "menu_phonebook").text
    if phone=="Phonebook":
        assert True, f"{phone} found"
    else:
        assert False, f"{phone} not found"

@then(u'check label of Config')
def con(context):
    con = context.driver.find_element(By.ID, "menu_config").text
    if con=="Config":
        assert True, f"{con} found"
    else:
        assert False, f"{con} not found"

@then(u'check label of TUC Notification')
def con(context):
    notif = context.driver.find_element(By.XPATH, "//*[@id='menu_notification']/p").text
    if notif == "Notification":
        assert True, f"{con} found"
    else:
        assert False, f"{con} not found"

    # time.sleep(1)
    # context.driver.close()