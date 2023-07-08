# Write your solution here:
class Item:

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name
    

class Suitcase:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: "Item"):
        if(self.weight() + item.weight() < self.__max_weight):
            self.__items.append(item)

    def __str__(self):
        ## Example solution:
        ## end_s = "s" if len(self.__items) != 1 else ""
 
        #return f"{len(self.__items)} item{end_s} ({self.weight()} kg)"
        if(len(self.__items) == 1):
            return f"{len(self.__items)} item ({self.weight()} kg)"
        return f"{len(self.__items)} items ({self.weight()} kg)"
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        current_weight = 0
        for item in self.__items:
            current_weight += item.weight()
        return current_weight
    
    def heaviest_item(self):
        heaviest_kg = 0
        heaviest = None
        if(len(self.__items) == 0):
            return None
        for item in self.__items:
            if(item.weight() > heaviest_kg):
                heaviest_kg = item.weight()
                heaviest = item
        return heaviest
    
class CargoHold:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: "Suitcase"):
        if(self.weight() + suitcase.weight() < self.__max_weight):
            self.__suitcases.append(suitcase)

    def weight(self):
        current_weight = 0
        for suitcase in self.__suitcases:
            current_weight += suitcase.weight()
        return current_weight
    
    def __str__(self):
        ## Example solution:
        ## word = "suitcases"
        ## if len(self.__suitcases) == 1:
            ##word = "suitcase"
 
        ## return f"{len(self.__suitcases)} {word}, space for {self.__max_weight-self.weight()} kg"
        if(len(self.__suitcases) == 1):
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.weight()} kg"
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()