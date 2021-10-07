from datetime import datetime

users_meeting_slot_list = []
users_available_slots = []
all_time_slots = set()

# Storing All Available Time Slots - ('10:00','11:00')
for slot in range(0,24):
    from_time = str(slot)
    to_time = str(slot+1)
    from_time_format = from_time + ':00' if len(from_time) == 2 else '0' + from_time + ':00'
    to_time_format = to_time + ':00' if len(to_time) == 2 else '0' + to_time + ':00'
    all_time_slots.add( ( from_time_format, to_time_format ) )

number_of_users = int(input("Enter number of users : "))
user_count = 1

# Obtaining Meeting slots from Input and passing to Users Meeting List
while user_count <= number_of_users:
    user_meeting_slots = set()
    number_of_meetings = int(input("Enter number of meetings for user "+str(user_count)+" : "))
    meetings_count = 1
    while meetings_count <= number_of_meetings:
        start_time = str(input("Enter start time for meeting "+ str(meetings_count)+" : "))
        end_time = str(input("Enter end time for meeting "+str(meetings_count)+" : "))
        try:
            start_time_format = datetime.strptime(start_time, "%d-%m-%Y %H:%M")
            end_time_format = datetime.strptime(end_time, "%d-%m-%Y %H:%M")
        except:
            print("Wrong Input format . please enter input in dd-mm-yyyy hh:mm format")
            continue
        start_time_hours = start_time_format.strftime("%H:%M")
        end_time_hours = end_time_format.strftime("%H:%M")
        user_meeting_slots.add((start_time_hours,end_time_hours))
        meetings_count = meetings_count + 1
    users_meeting_slot_list.append(user_meeting_slots)
    user_count = user_count + 1

# Obtaining Available Time Slots for User by referencing with All Time Slots
for user_meeting_slots in users_meeting_slot_list:
    user_slot = all_time_slots - user_meeting_slots
    users_available_slots.append(user_slot)

# Perform sorting on Avaliable Time Slots and display it
for user in range(len(users_available_slots)):
    user_slots = list(users_available_slots[user])
    user_slots = sorted(user_slots, key=lambda user_slot: int((user_slot[0].split(":"))[0]))
    print("Total Number of Available slots for user "+ str(user+1)+ " are "+str(len(user_slots)))
    print("Have a look at available slots")
    for (start_time,end_time) in user_slots:
        print(" slot from "+start_time +" to "+end_time)




