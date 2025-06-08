"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? A ValueError occurs when we try to enter something that is not a valid number
2. When will a ZeroDivisionError occur? When we divide to 0, we got ZeroDivisionError
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes. The code already avoids this error by using a try/except block to catch it.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero")
    else:
        fraction = numerator / denominator
        print(fraction)

except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
