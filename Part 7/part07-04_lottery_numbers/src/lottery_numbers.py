# Write your solution here
from random import shuffle
def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    shuffle(number_pool)
    weekly_draw = number_pool[0:amount]
    numbers = sorted(weekly_draw)
    return numbers

### Example solution

from random import randint
 
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
 
    return sorted(numbers)
    