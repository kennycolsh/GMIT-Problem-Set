# Ian McLoughlin, 2018-02-01
# Is it Wednesday?

import datetime

if datetime.datetime.today().weekday() == 2:
  print("Yay! It is Wednesday.")
else:
  
  print("Unfortunately it is not Wednesday.")
