"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    numbers_of_months = int(input("How many months? "))

    for month in range(1, numbers_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, numbers_of_months) # Call the new function




def print_income_report(incomes, numbers_of_months):
    """This function will print income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, numbers_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()