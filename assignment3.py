correct_pin = 1234
balance = 5000
max_attempt = 3

attempts = 0
logged_in = False

# PIN verification
while attempts < max_attempt:
    pin = int(input("Enter ATM PIN: "))

    if pin == correct_pin:
        print("Login successful")
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("Incorrect PIN")

if not logged_in:
    print("Too many incorrect attempts. Account locked.")

else:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                print(f"₹{amount:.2f} deposited successfully.")
                print(f"New Balance: ₹{balance:.2f}")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount > balance:
                print("Insufficient Balance")
            elif amount <= 0:
                print("Invalid withdrawal amount.")
            else:
                balance = balance - amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance:.2f}")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Please select 1-4.")
            
            
            
   ### ONLINE FOOD ORDERING SYSTEM #####         
            
            
menu = {
    1 : ("Pizza", 150),
    2 : ("Burger", 80),
    3 : ("Pasta", 120),
    4 : ("Cold Drink", 400)    
}

for number, item in menu.items():
    print(number, "-", item[0], "$", item[1])
    
choice = int(input("What do you want or order? "))
item_name = menu[choice][0]
price = menu[choice][1]

quantity = int(input("Enter quantity: "))
total = price * quantity

discount = 0
if total >= 500:
    discount = total * 0.10
else:
    discount = 0
    
discount = total * 0.10

after_discount = total - discount

dining = input("Dining option (Dine -in / Takeaway): ")

packing = 0

if dining == "Takeaway":
    packing = 20
    
final_bill = after_discount + packing
print("\n===== ORDER SUMMARY =====")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Packing Charges: ₹{packing}")
print(f"Final Bill: ₹{final_bill}")