def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    return total

def apply_discount(total):
    if total > 50000:
        return total * 0.90
    return total

cart = [
    {"item": "Laptop", "price": 50000, "qty": 1},
    {"item": "Mouse", "price": 500, "qty": 2}
]

total = calculate_total(cart)
final_amount = apply_discount(total)

print("Total Amount:", total)
print("Final Payable Amount:", final_amount)
