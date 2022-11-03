from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import new_quick_sms_input
import datetime

current_time = datetime.datetime.now()

from datetime import datetime
now = datetime.now()

@then(u'Schedule sms 100')
def step_impl(context):
    new_quick_sms_input.quick_sms(context)

