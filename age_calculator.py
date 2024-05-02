from datetime import datetime

date = input("Enter a date: ")

dt_obj1 = datetime.strptime(date, "%d/%m/%Y")

delta_time = datetime.today() - dt_obj1

print(f"{delta_time.days/365.25} years")
