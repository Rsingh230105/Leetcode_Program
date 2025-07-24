import datetime as dt
x=dt.datetime.now()
print(x)

print(dt.datetime(2026,1,23))

now=dt.datetime.now()# curreent date and time
year=now.strftime("%Y")
yearshort=now.strftime("%y")

print("year:",year,yearshort)

month=now.strftime("%m") #month number
print("month:",month)

day=now.strftime("%d")#day number
print("day:",day)

Mname=now.strftime("%b")
Mfullname=now.strftime("%B")
print("Month name short:",Mname,Mfullname)# december ka dec

hour=now.strftime("%H")
print("hour:",hour)#00-23

Hour=now.strftime("%I")
print("Hour:",Hour)#00-12


AmPm=now.strftime("%p")
print("AMPM:",AmPm)

minute=now.strftime("%M")
print("minute:",minute)






