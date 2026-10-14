#1 — Digital Clock

from datetime import datetime


def digital_clock():
    while True:
        now = datetime.now()

        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        print("\n===== DIGITAL CLOCK =====")
        print(f"Current Date: {current_date}")
        print(f"Current Time: {current_time}")

        user_input = input("\nPress Enter to update or type 'exit' to stop: ")

        if user_input.lower() == "exit":
            print("Clock stopped.")
            break


digital_clock()

#2 - Math Helper Tool

import math

number = float(input("Enter number: "))

square_root = math.sqrt(number)
square = math.pow(number, 2)
factorial = math.factorial(int(number))
ceil_value = math.ceil(number)
floor_value = math.floor(number)

print("\n===== MATH HELPER =====")
print(f"Square root: {square_root:.2f}")
print(f"Square: {square:.0f}")
print(f"Factorial: {factorial}")
print(f"Ceil: {ceil_value}")
print(f"Floor: {floor_value}")

# 3 — Safe Division Tool

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = first_number / second_number

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter numbers only")