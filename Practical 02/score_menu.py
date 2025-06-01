import random

def main():
    """Main function that takes user input and generates a random score to evaluate."""
    score = int(input("Scores: "))
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f'Random score: {random_score}, Result: {random_result}')

def determine_result(score):
    """Function takes an estimate and returns the result without output.
    Parameters:
        -score (int): A score between 0 and 100.
    Returns:
        - str: One of the result strings: "Invalid Score", "excellent", "Pass", or "Bad"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

main()