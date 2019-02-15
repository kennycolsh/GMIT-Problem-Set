#Problem 2 15-2-19 Kenny Colsh
#Get the day of the week
#check it the day "Startswith" a "T"
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
#https://www.w3schools.com/python/showpython.asp?filename=demo_ref_string_startswith
#https://stackoverflow.com/questions/17953940/yes-or-no-output-python
from datetime import date
import calendar
my_date = date.today()
print("Today is : " + calendar.day_name[my_date.weekday()])  

dayofweek =calendar.day_name[my_date.weekday()]


x = dayofweek.startswith("T")
if x :
  print("Yes - today begins with a T.")
else:
  print ("No - today does not begin with a T.")
  


