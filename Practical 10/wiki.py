"""
CP1404 Practical - Wikipedia API
Simple search tool using the wikipedia library
"""

import wikipedia

def main():
    """"""
    print("Wikipedia Search")
    while True:
        user_input = input("\nEnter page title: ").strip()
        if user_input == "":
            print("Thank you.")
            break

        try:
            # Try to fetch the page
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"\n{page.title}")
            print(wikipedia.summary(user_input, auto_suggest=False))
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.exceptions.PageError:
            print('Page id "{}" does not match any pages. Try another id!'.format(user_input))

if __name__ == "__main__":
    main()