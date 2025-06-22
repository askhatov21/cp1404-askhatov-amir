def main():
    """"""
    email_to_name = {}
    email = input("Email: ").strip()

    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n").strip().lower()

        if confirmation not in ["", "y", "yes"]:
            name = input("Name: ").title()

        email_to_name[email] = name
        email = input("Email: ").strip()

        print()
        for email, name in email_to_name.items():
            print(f"{name} ({email})")

    if __name__ == '__main__':
        main()