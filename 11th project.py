# 1. Create the tuple
prices = (250.300, 150, 400, 100, 350, 200)

# 2. Find and print the highest and lowest price
highest_price = max(prices)
lowest_price = min(prices)

print("Highest Price:", highest_price)
print("Lowest Price:", lowest_price)

# 3. Calculate and print the total sum of all prices
total_sum = sum(prices)
print("Total Sum of Prices:", total_sum)

# 4. Convert the tuple into a sorted list and print it
sorted_prices = sorted(prices)
print("Sorted Prices:", sorted_prices)

# 5. Try to modify an element in the tuple
try:
    prices[0] = 300  # Attempt to modify the first element
except TypeError as e:
    print("Error:",e)