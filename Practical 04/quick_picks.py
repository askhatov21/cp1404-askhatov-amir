import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 7

def main():
    """Ask the user for the number of quick picks and display that many sets of randomly generated numbers."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_formatted_quick_pick(quick_pick)


