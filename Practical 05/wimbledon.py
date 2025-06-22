FILENAME = "countries.csv"

def main():
    """Read Wimbledon data from a file, process the champions and countries,
and display the results including win counts and number of countries"""
    champion_data = read_data(FILENAME)
    champions_dict, countries_set = process_champions_data(champions_data)
    display_results(champions_dict, countries_set)


