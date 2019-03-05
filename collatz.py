##Problem Set Solution 4
def collatz(number):
	ans=""
	while number > 1:
		if number % 2 == 0:
			number = number//2
			print(number)
            
		else:
			number = (number*3)+1
			print(number)
           

number = input("Enter a number: ")

collatz(int(number))

