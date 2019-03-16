#Solution for problem 8
#https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
#7.2. Reading and Writing Files
#https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573


#user_input  = (input("Enter the name of the file : "))

with open('sol9.txt','r') as f:
    #f.readlines()
    #print(f.readlines())
    for i in f:
        print(i, end='')

with open('sol9.txt', 'r') as f:
    for count, line in enumerate(f, start=2):
        if count % 2 == 0:
            print(line)



