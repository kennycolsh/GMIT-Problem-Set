#Solution for problem 8

#import datetime lib
import datetime
import time

d_ =datetime.datetime.now()

dayOfWeek = d_.strftime("%A") + ", " + d_.strftime("%B")+ " " + d_.strftime("%d") + " "+d_.strftime("%Y") + " at "+ d_.strftime("%I:%M:%S %p")

print(dayOfWeek)