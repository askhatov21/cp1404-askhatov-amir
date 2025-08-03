from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Display existing guitars, allow user to add more, then save to file."""
    guitars = load_guitars()

    print("These are the existing guitars:")
    for guitar in guitars:
        print(guitar)

    print("\nSorted guitars: ")
    guitars.sort()  # Sort by year( if Guitar has a method __lt__)
    print("Sorted guitars:")
    for guitar in guitars:
        print(guitar)

    # Add a new guitars
    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        save_guitar_to_file(new_guitar)
        name = input("Name: ")

        print("\nFinal guitar list: ")
        for guitar in guitars:
            print(guitar)

def load_guitars():
    """Load guitars from file and return a list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars

def save_guitar_to_file(guitar):
    """Append a new guitar to the CSV file."""
    with open(FILENAME, 'a') as out_file:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()
