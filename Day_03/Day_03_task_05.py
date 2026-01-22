cart = [
    {"item": "Laptop", "price": 50000, "qty": 1},
    {"item": "Mouse", "price": 500, "qty": 2},
    {"item": "Keyboard", "price": 1500, "qty": 1}
]

total_amount = 0

for product in cart:
    total_amount += product["price"] * product["qty"]
print("Total Amount : ",total_amount)

# Apply discount if total > 50000
if total_amount > 50000:
    discount = total_amount * 0.10
    total_amount -= discount
    print("10% Discount Applied")

print("Final Amount to Pay:", total_amount)
