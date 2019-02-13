# Solution to problem 1 
#https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
user_input  = input("Please enter a positive integer:")
try:
   val = int(user_input)
   ans = 0
   print("Yes input string is an Integer.")
   if val > 0:
    print("Good Work its greater than 1!")
    i=1
    while i<= val:
        ans =ans+i
        i=i+1
    print(ans)
   else:
      print("Try and Pick a Number greater and 1")

        #print("Input number value is: ", val)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")