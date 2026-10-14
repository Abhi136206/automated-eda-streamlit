class Utility:

    def __init__(self, utility_name):
        self._utility_name = utility_name

    def display_info(self):
        print(f"Utility Name: {self._utility_name}")

    def run(self):
        print("Run method should be overridden by child classes.")

utility = Utility("Math Helper")
utility.display_info()
utility.run()

#2. Child Classes (Inheritance + Overriding)

from datetime import datetime
import math


class Utility:

    def __init__(self, utility_name):
        self._utility_name = utility_name

    def display_info(self):
        print(f"\nUtility: {self._utility_name}")

    def run(self):
        print("Run method should be overridden.")


class ClockUtility(Utility):

    def __init__(self):
        super().__init__("Digital Clock")

    def run(self):
        while True:
            now = datetime.now()

            print("\n===== DIGITAL CLOCK =====")
            print("Current Date:", now.strftime("%Y-%m-%d"))
            print("Current Time:", now.strftime("%H:%M:%S"))

            choice = input("\nPress Enter to refresh or type 'exit': ")

            if choice.lower() == "exit":
                break

class MathUtility(Utility):

    def __init__(self):
        super().__init__("Math Helper")
        self.number = 0

    def run(self):
        try:
            self.number = float(input("\nEnter a number: "))

            if self.number < 0:
                print("Square root is not available for negative numbers.")
            else:
                print("Square Root:", math.sqrt(self.number))

            print("Square:", math.pow(self.number, 2))

            if self.number >= 0 and self.number.is_integer():
                print("Factorial:", math.factorial(int(self.number)))
            else:
                print("Factorial: Only available for non-negative integers.")

            print("Ceil:", math.ceil(self.number))
            print("Floor:", math.floor(self.number))

        except ValueError:
            print("Error: Please enter a valid number.")

class DivisionUtility(Utility):

    def __init__(self):
        super().__init__("Division Calculator")

    def run(self):
        try:
            first_number = float(input("\nEnter first number: "))
            second_number = float(input("Enter second number: "))

            result = first_number / second_number

            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        except ValueError:
            print("Error: Please enter valid numbers.")

class ContactUtility(Utility):

    # Class variable
    filename = "contacts.txt"

    def __init__(self):
        super().__init__("Contact Saver")

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        with open(self.filename, "a") as file:
            file.write(f"{name} - {phone}\n")

        print("Contact saved successfully.")

    def view_contacts(self):
        try:
            with open(self.filename, "r") as file:
                contacts = file.read()

                if contacts:
                    print("\n===== SAVED CONTACTS =====")
                    print(contacts)
                else:
                    print("No contacts saved.")

        except FileNotFoundError:
            print("No contacts found.")

    def run(self):
        while True:
            print("\n===== CONTACT SAVER =====")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()

            elif choice == "2":
                self.view_contacts()

            elif choice == "3":
                break

            else:
                print("Invalid choice. Please select 1-3.")

def run_utility(utility):
    utility.display_info()
    utility.run()

clock = ClockUtility()
math_tool = MathUtility()
division = DivisionUtility()
contact = ContactUtility()

while True:

    print("\n==============================")
    print("       UTILITY SYSTEM")
    print("==============================")
    print("1. Digital Clock")
    print("2. Math Helper")
    print("3. Division Calculator")
    print("4. Contact Saver")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_utility(clock)

    elif choice == "2":
        run_utility(math_tool)

    elif choice == "3":
        run_utility(division)

    elif choice == "4":
        run_utility(contact)

    elif choice == "5":
        print("Thank you for using Utility System.")
        break

    else:
        print("Invalid choice. Please select 1-5.")
        
        
        
#3. Encapsulation Requirements

class Utility:

    def __init__(self, utility_name):
        self.__utility_name = utility_name

    # Getter
    def get_utility_name(self):
        return self.__utility_name

    # Setter
    def set_utility_name(self, utility_name):
        self.__utility_name = utility_name

    def display_info(self):
        print(f"Utility: {self.get_utility_name()}")

    def run(self):
        print("Run method should be overridden.")
        
        
# 4. Polymorphism
utilities = [
    ClockUtility(),
    MathUtility(),
    DivisionUtility(),
    ContactUtility()
]

for utility in utilities:
    utility.run()
    
#5. Menu System (Client Requirement)
class UtilityMenu:
    def __init__(self, utilities):
        self.utilities = utilities

    def display_menu(self):
        print("\n==============================")
        print("      SMART UTILITY SYSTEM")
        print("==============================")
        print("1. Digital Clock")
        print("2. Math Helper")
        print("3. Safe Division")
        print("4. Contact Saver")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "5":
                print("Thank you for using Smart Utility System.")
                break

            if choice in ["1", "2", "3", "4"]:
                utility = self.utilities[int(choice) - 1]
                utility.run()       # Polymorphism
            else:
                print("Invalid choice. Please select 1-5.")