# Write your solution here:
class LunchCard:

    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return(f"The balance is {self.balance:.1f} euros")
    
    def eat_lunch(self):
        if(self.balance >= 2.60):
            self.balance -= 2.60
    
    def eat_special(self):
        if(self.balance >= 4.60):
            self.balance -= 4.60

    def deposit_money(self, money: int):
        if(money < 0):
            raise ValueError("You cannot deposit an amount of money less than zeeo")
        self.balance += money
    
card_peter = LunchCard(20)
card_grace = LunchCard(30)
card_peter.eat_special()
card_grace.eat_lunch()
print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")
card_peter.deposit_money(20)
card_grace.eat_special()
print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")
card_peter.eat_lunch()
card_peter.eat_lunch()
card_grace.deposit_money(50)
print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")