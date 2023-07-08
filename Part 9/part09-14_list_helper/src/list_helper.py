# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        amount = 0
        char = 0
        for character in my_list:
            if(my_list.count(character) > amount):
                amount = my_list.count(character)
                char = character
        return char
    
    
    @classmethod
    def doubles(cls, my_list: list):
        amount = 0
        checked = []
        for char in my_list:
            if(my_list.count(char) >= 2 and char not in checked):
                amount += 1
                checked.append(char)
        return amount
    
### Example solution
class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles