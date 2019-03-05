##Problem Set Solution 4
def collatz(number):
	ans=""
	while number > 1:
		if number % 2 == 0:
			number = number//2
			print(number)
			ans = ans + ', ' + str(number)
            
		else:
			number = (number*3)+1
			print(number)
           
	return ans
number = input("Enter a number: ")

ans = collatz(int(number))

print(ans)

