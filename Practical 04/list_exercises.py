def main():
    """this function creates an empty list and prompts the user to enter 5 numbers"""
numbers = []
print("Please enter 5 numbers")

"""Prompt user for 5 numbers and append each to the list"""
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)


    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_of_number = sum(numbers) / len(numbers)


    """Printing the results"""
    print(f"The first number is {first_number }")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the number is {average_of_number}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = input("Usernames: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")



main()