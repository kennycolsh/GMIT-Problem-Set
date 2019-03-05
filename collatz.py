##Problem Set Solution 4
#create function collatz and pass it a variable number
def collatz(number):
	ans=""
	while number > 1:
		if number % 2 == 0:
			number = number//2
			ans = ans + ', ' + str(number)
            
		else:
			number = (number*3)+1
			ans = ans + ', ' + str(number)
#return the result of the function where the string var "ans"
# concats a number to a string           
	return ans
number = input("Enter a number: ")

ans = collatz(int(number))

print(ans)

