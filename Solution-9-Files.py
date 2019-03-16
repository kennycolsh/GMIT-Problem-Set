#Solution for problem 8
#https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
#7.2. Reading and Writing Files
#https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
#https://stackoverflow.com/a/44425842


user_input  = (input("Enter the name of the file : "))
print("Removing every second line, starting at the first line")
#start removing the first line
with open(user_input, 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 0:
            print(line)
print("Removing every second line, starting at the second line")
#start and remove the second line
with open(user_input, 'r') as f:
    for count, line in enumerate(f, start=2):
        if count % 2 == 0:
            print(line)


