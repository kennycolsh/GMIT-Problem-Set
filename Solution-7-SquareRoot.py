#Solution for problem 7

user_input  = input("Please enter a positive Float:")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(is_number(user_input))