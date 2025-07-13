from Practical_07 import
FILENAME = 'guitars.csv'

def main():
    """Display existing guitars and prompt user for new guitar to add and display"""
  guitars = load_guitars()

  print("These are the existing guitars: ")
  for guitar in guitars:
      print(guitar)

  print()
  guitars.sort() # Sort by year (if Guitar has a method __lt__)
  print("Sorted guitars:")
  for guitar in guitars:
      print(guitar)

    #Add a new guitars
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        save_guitar_to_file(new_guitar)
        name = input("Name: ")


def load_guitars():
    """Load guitars from file nad return a list of guitar objects"""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
        return guitars
main()