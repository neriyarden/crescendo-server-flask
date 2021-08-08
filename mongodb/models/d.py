import datetime

d = datetime.datetime.strptime('07/08/2021', "%d/%m/%Y").date()
x = datetime.time(23).strftime("%H:%M")
print(d)