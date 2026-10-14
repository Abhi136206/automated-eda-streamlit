Product = input("Enter product name :")
Price = float(input("Enter price : "))
quantity = int(input("Enter quantity : "))
discount = float(input("Enter discount percentage : "))
total = Price * quantity
discount_amount = total * (discount / 100)
final_amount = total-discount_amount
more_than_20 = discount >20
print("\n===== SHOPPING RECEIPT =====")
print(f"Item: {Product}")
print(f"Price per item: ₹{Price:.2f}")
print(f"Quantity: {quantity}")
print(f"More than 20%? {more_than_20}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")