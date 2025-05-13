file_path = "C:/Users/Student/Desktop/Python-lesson11/Python-lesson11/leximi.txt"

# file = open(file_path,"r")

# content = file.read()

# print(content)

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path, "r") as file:
    line1 = file.readline()
    print(line1)

with open(file_path, "w") as file:
    file.write("Hello World")

with open(file_path, "r") as file:
    file.seek(2)
    data = file.read()
    print(data)

import datetime

koha_aktuale = datetime.datetime.now()

print(koha_aktuale)

print("Year: ", koha_aktuale.year)
print("Month: ", koha_aktuale.month)
print("Day: ", koha_aktuale.day)
print("Hour: ", koha_aktuale.hour)
print("Minute: ", koha_aktuale.minute)
print("Second: ", koha_aktuale.second)
print("Micorsecond: ", koha_aktuale.microsecond)

koha_aktuale1 = datetime.datetime.now().date()
print(koha_aktuale1)
koha_aktuale2 = datetime.datetime.now().time()
print(koha_aktuale2)

time_object = datetime.date(2008, 2, 17)
print(time_object)

duration = datetime.timedelta(days=5,hours=3)
print(duration)

new_date = koha_aktuale + duration
print(new_date)

random_days = datetime.timedelta(days=1453)
random_date = koha_aktuale - random_days
print(random_date)

#challenge

current_date = datetime.datetime.now()
print("Year: ", current_date.year)
print("Month: ", current_date.month)
print("Day: ", current_date.day)
print("Hour: ", current_date.hour)
print("Minute: ", current_date.minute)
print("Second: ", current_date.second)
print("Micorsecond: ", current_date.microsecond)

days100 = datetime.timedelta(days=100)

new_date_previous = current_date - days100
print(new_date_previous)

new_date_after = current_date + days100
print(new_date_after)

with open(file_path, "w") as file:
    file.write(new_date_previous)
    file.write(new_date_after)