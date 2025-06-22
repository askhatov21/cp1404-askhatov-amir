FILENAME = "countries.csv"

def main():
    """Read Wimbledon data from a file, process the champions and countries,
and display the results including win counts and number of countries"""
    champion_data = read_data(FILENAME)
    champions_dict, countries_set = process_champions_data(process_champions_data())
    display_results(champions_dict, countries_set)


def read_data(filename):
    """Read file and return list of data rows."""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            champions_data.append(line.strip().split(","))
    return champions_data


def process_champions_data(champions_data):
    """Count champion wins and collect countries."""
    champions_dict = {}
    countries_set = set()

    for row in champions_data:
        champion = row[2]
        country = row[1]

        countries_set.add(country)
        champions_dict[champion] = champions_dict.get(champion, 0) + 1

    return champions_dict, countries_set

def display_results(champions_dict, countries_set):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in champions_dict.items():
        print(f"{champion:20} {wins}")

    countries_list = sorted(countries_set)
    print(f"\nThese {len(countries_list)} countries have won Wimbledon:")
    print(", ".join(countries_list))


if __name__ == "__main__":
    main()