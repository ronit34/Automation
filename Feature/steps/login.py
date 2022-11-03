from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# #*************** Chrome Driver *****************
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# **************** Chrome Headless ******************************
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# from webdriver_manager.chrome import ChromeDriverManager
# opt=Options()
# opt.add_argument("--headless")
#
# driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)

#************* Firefox ******************************
# driver = webdriver.Firefox(executable_path=r'/home/onexadmin/Downloads/geckodriver')

# ***************** Firefox Headless *********************************
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
#
# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(executable_path=r'/home/mehatab/behave_mehatab/lib/python3.8/geckodriver',options=options)

#**************** Screen SHot ***************************
# driver.get_screenshot_as_file(os.getcwd()+"/screenshots" + "Selenium_" + "Alilang"+".png")

@given(u'launch chrome browser')
def ChromeBrowserLaunch(context):

    try:
        context.driver = driver
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Onextel Homepage "{homepage}"')
def OpenHomepage(context, homepage):
    context.driver.maximize_window()
    try:
        context.driver.get(homepage)
    except NameError:
        print(f"{homepage} unable to load")
    else:
        print(f"{homepage} loaded successfully")

@then(u'verify that the inner text present on page')
def step_impl(context):
    # status = context.driver.find_element_by_xpath("/html/body/div/div/div[1]/p[2]").is_displayed()
    status = context.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/p[1]").is_displayed()
    assert status is True
    if status:
        print(f"{status}: message found")
    else:
        print(f"{status}: message not found")

@then(u'verify picture is present')
def VerifyPicture(context):
    # status = context.driver.find_element_by_xpath("/html/body/div/div/div[1]/img").is_displayed()
    status = context.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/img").is_displayed()
    assert status is True
    if status:
        print(f"{status}: info image is found")
    else:
        print("info image is found is not found")


@then(u'verify the message is present')
def VerifyMessage(context):
    # status = context.driver.find_element_by_xpath("/ html / body / div / div / div[1] / p[1]").is_displayed()
    status = context.driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/p[2]").is_displayed()
    assert status is True
    if status:
        print(f"{status}: message found")
    else:
        print(f"{status}: message not found")


@then(u'verify the user textbox is present')
def verifyUserTextbox(context):
    status = context.driver.find_element_by_id("email").is_displayed()
    assert status is True
    if status:
        print(f"{status}:user textbox present")
    else:
        print(f"{status}:user textbox not present")


@then(u'verify the password textbox is present')
def VerifyPasswordTextbox(context):
    status = context.driver.find_element_by_id("password").is_displayed()
    assert status is True
    if status:
        print(f"{status}:password textbox is present")
    else:
        print(f"{status}:password textbox is not present ")


@then(u'verify the user placeholder is present')
def UserPlaceHolder(context):
    status = context.driver.find_element_by_xpath("//*[@id='email']").is_displayed()
    assert status is True
    if status:
        print(f"{status}:user placeholder is present")
    else:
        print(f"{status}:user placeholder is not present")


@then(u'verify the Password placeholder is present')
def VerifyPasswordPlaceholder(context):
    status = context.driver.find_element_by_xpath("//input[@placeholder='Password']").is_displayed()
    assert status is True
    if status:
        print(f"{status}:password placeholder is present")
    else:
        print(f"{status}:password placeholder is not present")

@then(u'verify the eye button is present')
def step_impl(context):
    context.driver.find_element_by_id("show_password_eye").is_displayed()


@then(u'Verify Terms And Comditions Checkbox')
def VerifyTC(context):
    context.driver.implicitly_wait(20)
    status = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").is_displayed()
    assert status is True
    if status:
        print(f"{status}:Terms And Conditions Checkbox is present")
    else:
        print(f"{status}:Terms And Conditions Checkboxis not present")

@then(u'verify sign in button is present')
def VerifySignInButton(context):
    status = context.driver.find_element(By.ID, "login_button").is_displayed()
    assert status is True
    if status:
        print(f"{status}:sign in button is present")
    else:
        print(f"{status}:sign in button is not present")

    # time.sleep(1)
    # context.driver.close()
