def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [3, 8, 11, 20, 29]

for n in numbers:
    print(n, "is Prime" if is_prime(n) else "is Not Prime")
