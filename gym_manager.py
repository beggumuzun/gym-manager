import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "members.json"
PRICES = {"monthly": 30, "annual": 300}


def load_members():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_members():
    with open(DATA_FILE, "w") as file:
        json.dump(members, file, indent=4)


def show_menu():
    print("\n=== Gym Membership Manager ===")
    print("1. Add member")
    print("2. List members")
    print("3. Search member")
    print("4. Quit")


def ask_age():
    while True:
        text = input("Age: ").strip()
        if text.isdigit() and 0 < int(text) < 120:
            return int(text)
        print("Please enter a valid age (a number between 1 and 119).")


def calculate_price(package, age, is_student):
    price = PRICES[package]
    if age >= 65 or is_student:
        price = price * 0.8
    return price


def add_member():
    name = input("Name: ").strip().title()
    age = ask_age()
    is_student = input("Student? (yes/no): ").strip().lower() == "yes"
    package = input("Package (monthly/annual): ").strip().lower()
    while package not in PRICES:
        print("Invalid package. Please type 'monthly' or 'annual'.")
        package = input("Package (monthly/annual): ").strip().lower()

    price = calculate_price(package, age, is_student)

    member = {
        "name": name,
        "age": age,
        "student": is_student,
        "package": package,
        "price": price,
    }
    members.append(member)
    save_members()
    print(f"{name} added! Price: £{price:.2f}")


def list_members():
    if len(members) == 0:
        print("No members yet.")
        return

    print("\n--- Members ---")
    for member in members:
        print(f"{member['name']} | Age: {member['age']} | {member['package']} | £{member['price']:.2f}")


def search_member():
    query = input("Search name: ").strip().lower()
    found = False

    for member in members:
        if query in member["name"].lower():
            print(f"Found: {member['name']} | {member['package']} | £{member['price']:.2f}")
            found = True

    if not found:
        print("No member found.")


members = load_members()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_member()
    elif choice == "2":
        list_members()
    elif choice == "3":
        search_member()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")