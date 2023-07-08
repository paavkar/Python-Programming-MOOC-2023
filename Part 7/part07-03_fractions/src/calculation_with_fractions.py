# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
    frac = []
    for i in range(amount):
        frac.append(Fraction(f'1/{amount}'))
    return frac