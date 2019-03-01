lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%12 > 0):
        if(i%6==0):
            print(i)

#for i in range(lower,upper+1):   
   # if(i%12==0):
  #      print(i)

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")