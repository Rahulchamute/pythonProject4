

import datetime

# curr_time=datetime.datetime.now()
# print(curr_time)
#
# curr_time=datetime.datetime.today()
# print(curr_time)
#
# print(curr_time.year)
# print(curr_time.month)
# print(curr_time.day)
# print(curr_time.hour)
#
# curr_time=datetime.datetime.today().date()
# print(curr_time)
#
# curr_time=datetime.datetime.today().time()
# print(curr_time)


##timedelta
# curr_date=datetime.datetime.today().date()
# print(curr_date)
# new_date=curr_date+datetime.timedelta(days=1)
# print(new_date)
# new_date=curr_date+datetime.timedelta(days=-1)
# print(new_date)

# for i in range(1,11):
#     new_date=curr_date+datetime.timedelta(days=i)
#     print(new_date)

# for i in range(-10,10):
#     new_date=curr_date+datetime.timedelta(days=i)
#     print(new_date)
# new_date=curr_date+datetime.timedelta(weeks=1)
# print(new_date)
# new_date=curr_date+datetime.timedelta(weeks=-1)
# print(new_date)


# curr_time=datetime.datetime.today()
# print(curr_time)
# new_time=curr_time+datetime.timedelta(hours=5)
# print(new_time)

# curr_time=datetime.datetime.today()
# print(curr_time)
# new_time=curr_time+datetime.timedelta(seconds=600)
# print(new_time)

###strftime()
# curr_datetime=datetime.datetime.today()
# print(curr_datetime)
# print(curr_datetime.strftime("%Y"))
# print(curr_datetime.strftime("%y"))
# print(curr_datetime.strftime("%m"))
# print(curr_datetime.strftime("%B"))
# print(curr_datetime.strftime("%b"))
# print(curr_datetime.strftime("%d"))
# print(curr_datetime.strftime("%A"))
# print(curr_datetime.strftime("%a"))
# print(curr_datetime.strftime("%w"))
# print(curr_datetime.strftime("%j"))
# print(curr_datetime.strftime("%U"))
# print(curr_datetime.strftime("%p"))

# any_day=datetime.datetime(1990,5,15)
# print(any_day)
# # print(any_day.strftime("%Y-%d-%m"))
# # print(any_day.strftime("%Y-%m-%d"))
# # print(any_day.strftime("%Y/%m/%d"))
# #print(any_day.strftime("%y/%m/%d"))
# print(any_day.strftime("%Y/%B/%d"))
# print(any_day.strftime("%Y/%b/%d"))

##strptime

# d1="25-11-2020"
# date_format="%d-%m-%Y"
# new_date1=datetime.datetime.strptime(d1,date_format).date()
# print(new_date1)

# d2 = "25/11/2020"
# date_format = "%d/%m/%Y"
# new_date1 = datetime.datetime.strptime(d2,date_format).date()
# print("New Date2 :-",new_date1)


# date_list = ["17-02-2022","28/03/2022","17-02-22","2022-02-17","2022 Feb 17", "2022 February 17",
#             "2022 Aug 17", "17 Feb 22", "17 Feb 2022", "17/02/2022", "17/02/22", "17-05-2020"]
#
# date_format_list = ["%d/%m/%Y","%d-%m-%Y","%d-%m-%y","%Y-%m-%d", "%Y %b %d", "%Y %B %d", "%d %b %y",
#                    "%d %b %y", "%d %b %Y", "%d/%m/%y"]
# for date in date_list:
#     for date_format in date_format_list:
#         try:
#             new_date=datetime.datetime.strptime(date,date_format).date()
#             print(new_date)
#             break
#         except:
#             continue


date_list = ["17-02-2022","28/03/2022","17-02-22","2022-02-17","2022 Feb 17", "2022 February 17",
            "2022 Aug 17", "17 Feb 22", "17 Feb 2022", "17/02/2022", "17/02/22", "17-05-2020"]

date_format_list = ["%d/%m/%Y","%d-%m-%Y","%d-%m-%y","%Y-%m-%d", "%Y %b %d", "%Y %B %d", "%d %b %y",
                   "%d %b %y", "%d %b %Y", "%d/%m/%y"]
def get_date_object(date):
    for date_format in date_format_list:
        try:
            new_date=datetime.datetime.strptime(date,date_format).date()
            print(new_date)
            break
        except:
            continue
for date in date_list:
    get_date_object(date)
