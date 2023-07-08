# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to: "RealProperty"):
        if(self.square_metres > compared_to.square_metres):
            return True
        else:
            return False
        
    def price_difference(self, compared_to: "RealProperty"):
        own_price = self.square_metres * self.price_per_sqm
        compared_price = compared_to.square_metres * compared_to.price_per_sqm
        if(own_price > compared_price):
            return own_price - compared_price
        else:
            return compared_price - own_price
        
    def more_expensive(self, compared_to: "RealProperty"):
        own_price = self.square_metres * self.price_per_sqm
        compared_price = compared_to.square_metres * compared_to.price_per_sqm
        if(own_price > compared_price):
            return True
        return False
    
### Example solution
def price_difference(self, compared_to):
    # Function abs returns absolute value
    difference = abs((self.price_per_sqm * self.square_metres) - (compared_to.price_per_sqm * compared_to.square_metres))
    return difference
 
def more_expensive(self, compared_to):
    difference = (self.price_per_sqm * self.square_metres) - (compared_to.price_per_sqm * compared_to.square_metres)
    return difference > 0