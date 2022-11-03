#
i = 30
count=0
while i <= 40:
  if(i%2!=0):
      count=count+i

  i += 1
print(count)
#
# left=1
# right=10
# k=3
# count=0
# while(left<=right):
#     if(left%k==0):
#         count=count+left
#     else:
#         print(count)
# left=left+1
#
# if(count%3==0):
#     c=count+
#
#
#
# # import colorama
# # from colorama import Fore, Back, Style
# #
# # colorama.init()
# #
# # text = "The quick brown fox jumps over the lazy dog"
# #
# # print(Fore.RED + text)
# # print(Back.GREEN + text + Style.RESET_ALL)
# # print(text)
#
#
#
#
#
# # from behave import *
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# #
# #
# # @then(u'login by using css selector')
# # def step_impl(context):
# #
# #     #If we are using id in css selector then use #before id
# #
# #     # button = context.driver.find_element(By.CSS_SELECTOR,'#login_button')
# #     # context.driver.execute_script("arguments[0].click();", button)
# #
# #     button = context.driver.find_element(By.CSS_SELECTOR,"class.btn sign-in form-button wfid_loginbtn wfid_temp423810 textbox")
# #     context.driver.execute_script("arguments[0].click();", button)