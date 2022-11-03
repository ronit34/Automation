import time
from behave import *
from selenium.webdriver.support.select import Select

@then(u'select Promo from dropdown')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element_by_xpath("//*[@id='pills-campaign']/div[1]/div[2]/div/div/div/div[2]/div/select"))
    select.select_by_visible_text('Promotional')

@then(u'check Scrub Dnd checkbox is preselected in API')
def step_impl(context):
    time.sleep(2)
    checkbox = context.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/label/input").is_selected()
    if checkbox == True:
        assert True
    else:
        assert False, f"checkbox is not selected"



