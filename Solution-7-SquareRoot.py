#Solution for problem 7
#https://stackoverflow.com/questions/34425583/how-to-check-if-string-is-int-or-float-in-python-2-7?answertab=votes#tab-top
#import the math lib

import math
user_input  = (input("Please enter a positive Float:"))


def is_number(s):
    try:
        #see if can be converted to a float
        float(s)

        return True
    except ValueError:
        #return false if it cannot be converted to a float.
        return False

print(is_number(user_input))

#check if returned value is a float
if (is_number(user_input)) == True:
        print("Its a float.")
        #ans = math.sqrt(s)
        #print(ans)