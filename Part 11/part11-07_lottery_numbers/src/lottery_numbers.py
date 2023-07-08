# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:

    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.numbers])
    
    def hits_in_place(self, numbers: list):
        return [numbers[i] if numbers[i] in self.numbers else -1 for i in range(len(numbers))]