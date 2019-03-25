# GMIT-Problem-Set
THis respository contains my solutions to the problem set 2019 for the module programming and scription.
Course questions
[See here for the instructions] (https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf)

##How to download this respository

1.Go to github (https://github.com/kennycolsh/GMIT-Problem-Set.git)
2.click the download button


##How to run the code

1. Install python.


##What each file contains
1. Solution-1.py contains my solution for problem 1 in the problem set.
  I also put some simple error checking in to ensure that user of this code inputs a positive integer.

##Referances used:-
#[https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard]

2. Solution-2.py contains my solution for problem 2 in the problem set.
  I also added code to tell the user of this code what day of the week it is.

##Referances used:-
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
#https://www.w3schools.com/python/showpython.asp?filename=demo_ref_string_startswith
#https://stackoverflow.com/questions/17953940/yes-or-no-output-python

3. Solution-3.py contains my solution for problem 3 in the problem set.
<<<<<<< HEAD
 I also added some functioality to allow the user to enter in the upper and lower limit of the program then they can enter in the number that needs to get divided.
 

##Referances used:-
[https://www.sanfoundry.com/python-program-print-numbers-range-divisible-given-number/]


4. Solution-4.py contains my solution for problem 4 in the problem set.(collatz)
 When the user enters in a number it calls the collatz function the appends onto a string "ans" 
 and then returns and prints the result (ans)
 

##Referances used:-

5. Solution-5.py contains my solution for problem 5 in the problem set.
to check if a number is a prime number and returns true or false.
I also used code from my solution 1 that checks if the user enters a valid integer.
the code also stays in the loop untill the user enters a number less than 1
 

##Referances used:-
https://linuxconfig.org/function-to-check-for-a-prime-number-with-python

6. Solution-6-SplitString.py contains my solution for problem 6 in the problem set.
Write a program that takes a user input string and outputs every second word.
I also used code from my solution 1 to take an input from the user.I used a function and caled it to 
split the input string and also to see if the user entered a sentence with just one word in it.
 

##Referances used:-
https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word

7. Solution-7-SquareRoot.py contains my solution for problem 7 in the problem set.
Write a program that that takes a positive floating point number as input and outputs
an approximation of its square root.
One trick i noticed at the end was I had to convert the float back to a strinf to concat it for printing.
 

##Referances used:-
#https://stackoverflow.com/questions/34425583/how-to-check-if-string-is-int-or-float-in-python-2-7?answertab=votes#tab-top
#import the math lib
#https://stackoverflow.com/posts/3400987/edit for rounding

8. Solution-8-DateFormat.py contains my solution for problem 8 in the problem set.
Write a program that outputs today’s date and time in the format ”Monday, January
10th 2019 at 1:15pm”. The trick was getting the th,rd,nd etc. and I used an array
 

##Referances used:-
#Solution for problem 8
#referances https://stackoverflow.com/a/18944849
    #%a  Locale’s abbreviated weekday name.
    #%A  Locale’s full weekday name.      
    #%b  Locale’s abbreviated month name.     
    #%B  Locale’s full month name.
    #%c  Locale’s appropriate date and time representation.   
    #%d  Day of the month as a decimal number [01,31].    
    #%f  Microsecond as a decimal number [0,999999], zero-padded on the left
    #%H  Hour (24-hour clock) as a decimal number [00,23].    
    #%I  Hour (12-hour clock) as a decimal number [01,12].    
    #%j  Day of the year as a decimal number [001,366].   
    #%m  Month as a decimal number [01,12].   
    #%M  Minute as a decimal number [00,59].      
    #%p  Locale’s equivalent of either AM or PM.
    #%S  Second as a decimal number [00,61].
    #%U  Week number of the year (Sunday as the first day of the week)
    #%w  Weekday as a decimal number [0(Sunday),6].   
    #%W  Week number of the year (Monday as the first day of the week)
    #%x  Locale’s appropriate date representation.    
    #%X  Locale’s appropriate time representation.    
    #%y  Year without century as a decimal number [00,99].    
    #%Y  Year with century as a decimal number.   
    #%z  UTC offset in the form +HHMM or -HHMM.
    #%Z  Time zone name (empty string if the object is naive).    
   # %%  A literal '%' character.

#https://stackoverflow.com/a/52045942
#to help with the function to get st,nd,th,etc 

9. Solution-9-FIles.py contains my solution for problem 9 in the problem set.
Write a program that reads in a text file and outputs every second line. The program
should take the filename from an argument on the command line.
 

##Referances used:-
#Solution for problem 9
#https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
#7.2. Reading and Writing Files
#https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
#https://stackoverflow.com/a/44425842

10. Solution-10-FIles.py contains my solution for problem 10 in the problem set.
Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4].

I also added some legends and a title to the plot
 

##Referances used:-
#https://pythonspot.com/matplotlib-legend/
also used the videos from week 9
#Solution for problem 10



