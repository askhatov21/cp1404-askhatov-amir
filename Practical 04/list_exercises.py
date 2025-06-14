def main():
    """this function creates an empty list and prompts the user to enter 5 numbers"""
numbers = []
print("Please enter 5 numbers")

"""Prompt user for 5 numbers and append each to the list"""
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)


    first_number = number[0]
    last_number = number[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_of_number = sum(numbers) / len(numbers)









main()