# Solution to problem 1 
#https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard

quit =0
while  quit < 1:

   try:
         user_input  = input("Please enter a positive integer:")
         val = int(user_input)
         ans = 0
            #print("Yes input string is an Integer.")
         if val > 0:
            print("Good Work its an Interger and greater than 1!")
            i=1
            while i<= val:
               ans =ans+i
               i=i+1
            print(ans)             
         else:
               print("Try and Pick a Number greater and 0")

         quit1  = input("Enter an interger less than 1 to quit")
         quit = int(quit1)
         print(quit)
         #print("Input number value is: ", val)
   except ValueError:
         print("No.. input string is not an Integer. It's a string")


  
  
