#
# import datetime
#
# # using now() to get current time
# current_time = datetime.datetime.now()
# print (current_time.hour+1)
# print (current_time.minute+1)
# print (current_time.day)
# # print (current_time.datetime.now)
#
#
from datetime import datetime,timedelta
#
now = datetime.now()
# # print(now)
# # current_time = now.strftime("%H:%M:%S")
# # print("Current Time =", current_time)
import datetime
# from datetime import date
current_time = datetime.datetime.now()
# # from datetime import date
# # today = date.today()
# # d1 = today.strftime("%d/%m/%Y")
# # print(d1)
# t=str(current_time + timedelta(minutes=1))
# # a= current_time + timedelta(minutes=3)
# print(t)
# hours = int(current_time.minute)
minutes = str(current_time.minute+1)

# a = (current_time.minute + 3)
print(minutes)