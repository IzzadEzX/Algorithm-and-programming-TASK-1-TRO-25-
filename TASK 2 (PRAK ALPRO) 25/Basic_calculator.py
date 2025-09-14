#program for calculator
user_input = input("Do you wanna use calculator? (Y/N) ")
while user_input.upper() == 'Y':
    input_1 = int(input("Enter your first number = "))
    operator_user = input("(+, -, *, /) = ")
    input_2 = int(input("Enter your second number = "))

    if operator_user == '+':
        result = input_1 + input_2
    elif operator_user == '-':
        result = input_1 - input_2
    elif operator_user == '*':
        result = input_1 * input_2
    elif operator_user == '/':
        if input_2 == 0:
            result = "Cannot devide by zero"
        else:
            result = input_1/input_2
    else:
        result = "Invalid operator"
    #Print result
    print("The result is ", result)
    result = 0
    #Ask user again
    user_input = input("Do you wanna use calculator again? (Y/N) ")

print("Thanks for using our provide")
    
