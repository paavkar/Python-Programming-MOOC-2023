# Write your solution here
def prime_numbers():
    number = 2
    while True:
        prime = True
        for i in range(2, number):
            if(number % i == 0):
                prime = False
                break
        if(prime):
            yield number
        number += 1

### Example solution
def prime_numbers():
    number = 1
    while True:
        if is_prime(number):
            yield number
        number += 1
 
# Helper method for checking if number is prime
def is_prime(number: int):
    if number < 2:
        return False
    # Possible divisor is between 2 and number-1
    for i in range(2, number):
        if number % i == 0:
            return False
    return True