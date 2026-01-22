def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance")
        return balance
    return balance - amount

balance = 10000

balance = deposit(balance, 5000)
balance = withdraw(balance, 3000)

print("Final Balance:", balance)
