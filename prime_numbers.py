def is_prime(number):
    "check if a number is prime."
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

for number in range(2, 101):
    if is_prime(number):
         print(number)

