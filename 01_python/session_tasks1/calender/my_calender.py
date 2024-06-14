import calendar
month=int(input("enter month : "))
year=int(input("enter year : "))
if((month>0 and month <=12)and year>0):
    cal=calendar.month(year,month)
    print(cal)
else:
    print("wrong entering month or year , try again")
    