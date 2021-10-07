from datetime import datetime

user_meetings_list = []
all_time_slots = set()
for slot in range(0,24):
    all_time_slots.add((str(slot)+':00',str(slot+1)+':00'))
print("all_time_slots is ",all_time_slots)
n = int(input("Enter number of users : "))
for i in range(n):
    user_meetings = set()
    m = int(input("Enter number of meetings for "+str(i+1)+" user : "))
    for j in range(m):
        from_time = str(input("Enter start time for "+ str(j+1)+" meeting : "))
        to_time = str(input("Enter to time for "+str(j+1)+" meeting : "))
        from_time_format = datetime.strptime(from_time, "%d-%m-%Y %H:%M")
        from_time_hours = from_time_format.strftime("%H:%M")
        to_time_format = datetime.strptime(to_time, "%d-%m-%Y %H:%M")
        to_time_hours = to_time_format.strftime("%H:%M")
        user_meetings.add((from_time_hours,to_time_hours))
    user_meetings_list.append(user_meetings)
print("user_meetings_list is ",user_meetings_list)
user_available_slots = []
for user in user_meetings_list:
    user_slot = all_time_slots - user
    user_available_slots.append(user_slot)
print("user_available_slots is ",user_available_slots)
for user in user_available_slots:
    l = list(user)
    print("list is ",l)
    l = sorted(l, key=lambda x: int((x[0].split(":"))[0]))
    print("After sort list is ",l)
    print("Total Number of Available slots are ",len(l))
    print("Have a look at available slots")
    for (from_time,to_time) in l:
        print(" slot from "+from_time +" to "+to_time)




