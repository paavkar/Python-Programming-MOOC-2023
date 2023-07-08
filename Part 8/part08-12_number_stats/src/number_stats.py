# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        if(len(self.numbers) > 0):
            return sum(self.numbers)
        else:
            return 0
        
    def average(self):
        if(len(self.numbers) > 0):
            return sum(self.numbers)/len(self.numbers)
        else:
            return 0.0

def main():
    stats = NumberStats()
    even = NumberStats()
    odd = NumberStats()
    #stats.add_number(3)
    #stats.add_number(5)
    #stats.add_number(1)
    #stats.add_number(2)
    while True:
        number = int(input("Please type in integer numbers: "))
        if(number == -1):
            break
        stats.add_number(number)
        if(number % 2 == 0):
            even.add_number(number)
        else:
            odd.add_number(number)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", even.get_sum())
    print("Sum of odd numbers:", odd.get_sum())
main()