from datetime import datetime

my_date = "05-10-2021 12:00"

d = datetime.strptime(my_date, "%d-%m-%Y %H:%M")
print(d)
# dt = d.strftime("%H")
# print(dt)
# my_date1 = "05-10-2021 13:00"

# d1= datetime.strptime(my_date1, "%d-%m-%Y %H:%M")
# print(d1)
# dt1 = d1.strftime("%H")
# print(dt1)
# print("type is ",type(dt))

# tup = [(dt,dt1)]
# tup_list = [('1','2'),('12','13')]
# print(tup)

# for t in tup:
#     print("t is ",t)
#     if t in tup_list:
#         print("true")