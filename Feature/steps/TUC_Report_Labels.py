import time
from behave import *
from selenium.webdriver.common.by import By

# @then(u'click on Report')
# def credit(context):
#     time.sleep(2)
#     context.driver.find_element_by_xpath("//*[@id='menu_report']/p").click()

@then(u'check text of Mis under report')
def mis(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("pills-mis-data-tab").text

    if text == "MIS":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on MIS')
def campaigns(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-mis-data-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text of Mis under report TUCs')
def tucs(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Mis under report Month')
def month(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[2]/label").text

    if text == "Month":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Mis under report Year')
def year(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[3]/label").text

    if text == "Year":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Mis under report Search')
def search(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[4]/input").get_attribute('value')

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Mis under report Download')
def download(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[2]/div/div/a").text

    if text == "Download":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Summary')
def tucs(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-summary-tab").text

    if text == "Summary":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on summary tab in report tab')
def tucs(context):
    time.sleep(2)
    context.driver.find_element_by_id("pills-summary-tab").click()

@then(u'check text under report in search TUCs')
def tucs(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text under report in search From')
def frm(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text under report in search To')
def to(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text under report in search campaign')
def to(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[4]/label").text

    if text == "Campaign Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check text under report in search Limit')
# def limit(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[5]/label").text
#
#     if text == "Limit":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check text of Campaign Summary under report')
def campaign_summary(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-campaign-summary-tab").text

    if text == "Campaign Summary":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on campaign summary tab')
def campaigns(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-campaign-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text TUCs Campaign Summary under report')
def tucs(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/label").text
    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text From Campaign Summary under report')
def frm(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text To Campaign Summary under report')
def to(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Campaign Name Campaign Summary under report')
def campaign_name(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/div[1]/label").text

    if text == "Campaign Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Limit Campaign Summary under report')
def to(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/div[2]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Search Campaign Summary under report')
def search(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='search']").get_attribute('value')

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Download Campaign Summary under report')
def download(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "dropdownMenuLink").text

    if text == "Download":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of search tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-search-tab").text

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on search tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check text TUCs in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[1]/div/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text From in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[1]/div/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text To in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[1]/div/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Limit in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[1]/div/div[4]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Mobile in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[2]/div/div[1]/label").text

    if text == "Mobile":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Sender ID in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[2]/div/div[2]/label").text

    if text == "Sender ID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text UUID in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[2]/div/div[3]/label").text

    if text == "UUID":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text Source Type in search tab under report')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-search']/div[2]/div/div[4]/label").text

    if text == "Source Type":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Sender ID Summary under report')
def sender_id(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-daily-summary-tab").text

    if text == "Sender ID Summary":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Sender ID Summary')
def campaigns(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-daily-summary-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text of Sender ID Summary under report TUCs')
def tucs(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Sender ID Summary under report From')
def frm(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Sender ID Summary under report To')
def to(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Sender ID Summary under report Sender ID(optional)')
def sender_id(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-daily-summary']/div[2]/div/div[1]/label").text

    if text == "Sender ID(optional)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Sender ID Summary under report Search')
def search(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='search']").get_attribute('value')

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Clicker Data')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-clicker-data-tab").text

    if text == "Clicker Data":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the Clicker Data tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-clicker-data-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text of Clicker Data under report TUCs')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[1]/div/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Clicker Data under report From')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[1]/div/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Clicker Data under report To')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[1]/div/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Clicker Data under report Mobile')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-clicker-data']/div[1]/div/div[4]/label").text
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[2]/div/div[1]/label").text

    if text == "Mobile":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

# @then(u'check text of Clicker Data under report Campaign Name')
# def step_impl(context):
#     time.sleep(1)
#     text = context.driver.find_element_by_xpath(
#         "//*[@id='pills-clicker-data']/div[2]/div/div[1]/label").text
#
#     if text == "Campaign Name":
#         assert True, f"{text} is present"
#     else:
#         assert False, f"{text} is not present"

@then(u'check text of Clicker Data under report Limit')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[2]/div/div[2]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check text of Clicker Data under report Search')
def step_impl(context):
    time.sleep(1)
    # text = context.driver.find_element_by_xpath(
    #     "//*[@id='pills-clicker-data']/div[1]/div/div[5]/input").get_attribute('value')
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-clicker-data']/div[2]/div/div[3]/input").get_attribute('value')

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report')
def download_data(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "pills-download-data-tab").text

    if text == "Download Data":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on the Schedule Campaigns tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("pills-campaign-tab")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check text of Schedule Campaigns under report TUCs')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[1]/div[1]/label").text

    if text == "TUCs":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Schedule Campaigns under report From')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[1]/div[2]/label").text

    if text == "From":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Schedule Campaigns under report To')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[1]/div[3]/label").text

    if text == "To":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Schedule Campaigns under report Campaign Name')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[1]/div[4]/label").text

    if text == "Campaign Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Schedule Campaigns under report Limit')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[1]/div[5]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check text of Schedule Campaigns under report Search')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id(
        "search").get_attribute("value")

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


#************************ Define in report_mis_download *********************

@then(u'click on Download Data')
def campaigns(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-download-data-tab")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check  text of Download Data under report Request Time')
def request_time(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[1]").text

    if text == "Request Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report File Creation Time')
def file_creation_time(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[2]").text

    if text == "File Creation Time":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report Report Type | DocType')
def report_type(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[3]").text

    if text == "Report Type | DocType":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report File Name')
def file_name(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[4]").text

    if text == "File Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report Filters')
def filters(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[5]").text

    if text == "Filters":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report Status')
def status(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[6]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check  text of Download Data under report Download')
def download(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/table/tbody/tr/th[7]").text

    if text == "Download":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()