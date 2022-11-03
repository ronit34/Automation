import time
from behave import *
from selenium.webdriver.common.by import By


# @then(u'Enter Username "ICICIAdmin" and password "ali"')
# def step_impl(context):
#     context.driver.find_element_by_id("email").send_keys("ICICIAdmin")
#     context.driver.find_element_by_id("password").send_keys("ali")
#     time.sleep(2)

@then(u'click on the config tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='menu_config']/p")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check the config text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[1]/p[1]").text

    if text == "Config":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the blacklist category button text')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-tab']/li[1]").text

    if text == "Blacklist Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Category Name text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[2]").text

    if text == "Category Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Total Numbers is present')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[3]").text

    if text == "Total Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Category Description text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[4]").text

    if text == "Category Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Status text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[5]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Action text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[6]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on the new blacklist button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='add_blacklist']")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if Create Black List Category text is present inside new blacklist button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]/p[1]").text

    # if text == "Create Black List Category":
    if text == "Add Blacklist Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Name text is present inside new blacklist button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[1]/label").text

    # if text == "Category Name":
    if text == "Category Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Status text is present inside new blacklist button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[2]/label").text

    if text == "Category Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Description text is present inside new blacklist button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[3]/label").text

    # if text == "Category Description":
    if text == "Category Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of create button inside new blacklist button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='create_blacklist']").get_attribute('value')

    # if text == "Create":
    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on the cancel button of new blacklist button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_xpath("//*[@id='cancel_modal']")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check the text of BlackList Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='blacklist_num_tab']").text

    if text == "BlackList Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Add Blacklist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='add_blacklist']").text

    if text == "Add Blacklist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Name text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-blacklist-number']/div[1]/div/div[1]/label").text

    if text == "Name (Optional)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Description text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-blacklist-number']/div[1]/div/div[2]/label").text

    if text == "Description(Optional)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Category text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-blacklist-number']/div[1]/div/div[3]/label").text

    # if text == "Category":
    if text == "Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Number text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-blacklist-number']/div[1]/div/div[4]/label").text

    # if text == "Number":
    if text == "Number*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of add button in tuc config blacklist')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='add-blacklist-number']").get_attribute('value')

    if text == "Add Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Select Category text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-blacklist-number']/div[2]/div[1]/div[1]/label").text

    if text == "Select Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Select Number(Optional) text is present or not inside blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-blacklist-number']/div[2]/div[1]/div[2]/label").text

    if text == "Number(Optional)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of limit in blacklist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-blacklist-number']/div[2]/div[1]/div[3]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of search in blacklist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add").get_attribute("value")

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Delete Selected in blacklist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("delete-blacklist-number").get_attribute("value")

    if text == "Delete Selected":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Delete All in blacklist number')
def step_impl(context):
    time.sleep(1)
    # Delete Selected & Delete All have same ID and same Xpath
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/input").get_attribute("value")

    if text == "Delete All":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Upload Blacklist Number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='update_blacklist']").text

    if text == "Upload Blacklist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on Upload Blacklist Number')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("update_blacklist")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text of Downlaod Sample file of Blacklist Number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-upload-blacklist-numebr']/div[1]/div[2]/p").text

    if text == "Download Sample File":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Select Category Blacklist text is present or not is present inside category blacklist')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-upload-blacklist-numebr']/div[2]/div/div[1]/label").text

    # if text == "Select Category":
    if text == "Select Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of upload button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("upload_all").get_attribute('value')

    if text == "Add Records to Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Download Blacklist Number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='download_blacklist']").text

    if text == "Download Blacklist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'click on Download Blacklist Number')
def step_impl(context):
    button = context.driver.find_element_by_id("download_blacklist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if  Category text is present or not inside download blacklist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[1]/div/div[1]/label").text

    # if text == "Category":
    if text == "Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  File Type text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[1]/div/div[2]/label").text

    # if text == "File Type":
    if text == "File Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if download button text is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='download_blacklist_number']").get_attribute('value')

    if text == "Download":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Whitelist Category tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='whitelist_cat_tab']").text

    if text == "Whitelist Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Name text is present inside Whitelist Category tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[2]").text

    if text == "Category Name":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Total numbers text is present inside Whitelist Category tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[3]").text

    if text == "Total Numbers":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Description text is present inside Whitelist Category tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[4]").text

    if text == "Category Description":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Status text is present inside Whitelist Category tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[5]").text

    if text == "Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Action text is present inside Whitelist Category tab or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='tab_content']/table/tbody/tr/th[6]").text

    if text == "Action":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of new whilelist button and click on it if it is present')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='add_whitelist']").text

    if text == "+ New Whitelist":
        button = context.driver.find_element_by_xpath("//*[@id='add_whitelist']")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Create Whitelist Category text is present inside new whilelist button or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[1]/p[1]").text

    # if text == "Create Whitelist Category":
    if text == "Add Whitelist Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Name text is present inside new whilelist button or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[1]/label").text

    # if text == "Category Name":
    if text == "Category Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Status text is present inside new whilelist button or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[2]/label").text

    if text == "Category Status":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if Category Description text is present inside new whilelist button or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div[3]/label").text

    # if text == "Category Description":
    if text == "Category Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if text or create button is present or not')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='create_whitelist']").get_attribute('value')

    # if text == "Create":
    if text == "Add":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of cancel button and click on it if it is present')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='cancel_modal']").get_attribute('value')

    if text == "Cancel":
        button = context.driver.find_element_by_xpath("//*[@id='cancel_modal']")
        context.driver.execute_script("arguments[0].click();", button)
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='whitelist_num_tab']").text

    if text == "Whitelist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Add Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='add_whitelist']").text

    if text == "Add Whitelist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Name text is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-whitelist-number']/div[1]/div/div[1]/label").text

    # if text == "Name":
    if text == "Name*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Description text is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-whitelist-number']/div[1]/div/div[2]/label").text

    # if text == "Description":
    if text == "Description*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Category text is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-whitelist-number']/div[1]/div/div[3]/label").text

    # if text == "Category":
    if text == "Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Number text is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-add-whitelist-number']/div[1]/div/div[4]/label").text

    # if text == "Number":
    if text == "Number*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of add button in tuc config Whitelist')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add-whitelist-number").get_attribute('value')

    if text == "Add Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if  Select Category text second is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-whitelist-number']/div[2]/div[1]/div[1]/label").text

    if text == "Select Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if  Select Number(Optional) text is present or not inside whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-whitelist-number']/div[2]/div[1]/div[2]/label").text

    if text == "Number(Optional)":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text limit inside Add whitelist number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-add-whitelist-number']/div[2]/div[1]/div[3]/label").text

    if text == "Limit":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of search in whitelist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("add").get_attribute("value")

    if text == "Search":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Delete Selected in whitelist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("delete-whitelist-number").get_attribute("value")

    if text == "Delete Selected":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Delete All in whitelist number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/input").get_attribute("value")

    if text == "Delete All":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the text of Upload Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='update_whitelist']").text

    if text == "Upload Whitelist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'click on Upload Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element_by_id("update_whitelist")
    context.driver.execute_script("arguments[0].click();", button)

@then(u'check text of Downlaod Sample file of Whitelist Number')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "//*[@id='pills-upload-whitelist-numebr']/div[1]/div[2]/p").text

    if text == "Download Sample File":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check if Select Category Whitelist inside Upload Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-upload-whitelist-numebr']/div[2]/div/div[1]/label").text

    # if text == "Select Category":
    if text == "Select Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

@then(u'check the upload button text inside Upload Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_id("upload_all").get_attribute('value')

    if text == "Add Records to Category":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the text of Download Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='download_whitelist']").text
    if text == "Download Whitelist Number":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'Click on Download Whitelist Number')
def step_impl(context):
    button = context.driver.find_element_by_id("download_whitelist")
    context.driver.execute_script("arguments[0].click();", button)


@then(u'check if text Category is present or not inside Download Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[1]/div/div[1]/label").text

    # if text == "Category":
    if text == "Category*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check if text File Type is present or not inside Download Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath("//*[@id='pills-daily-summary']/div[1]/div/div[2]/label").text

    # if text == "File Type":
    if text == "File Type*":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then(u'check the Download button text inside Download Whitelist Number tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div/div[1]/div/div[3]/input").get_attribute('value')

    if text == "Download":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    # time.sleep(1)
    # context.driver.close()
