# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        return value1 == value2
    
    def __lt__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        return value1 < value2

    def __gt__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        return value1 > value2

    def __ne__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        return value1 != value2
    
    def __add__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        value3 = (value1 + value2) / 100
        value3 = f"{value3:.2f}"
        euros, cents = value3.split(".")
        return Money(int(euros), int(cents))
        

    def __sub__(self, another):
        value1 = self.__euros * 100 + self.__cents
        value2 = another.__euros * 100 + another.__cents
        if(value1 - value2 < 0):
            raise ValueError("a negative result is not allowed")
        value3 = (value1 - value2) / 100
        value3 = f"{value3:.2f}"
        euros, cents = value3.split(".")
        print(value3)
        return Money(int(euros), int(cents))
    
## Example solution
# Helper method for returning the value in cents
    # --> makes the comparisons easier
    def __value(self):
        return self.__euros * 100 + self.__cents
 
    # Another helper method which converts cents to value
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
 
    def __eq__(self, other: "Money"):
        return self.__value() == other.__value()
 
    def __lt__(self, other: "Money"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "Money"):
        return self.__value() > other.__value()
 
    def __ne__(self, other: "Money"):
        return self.__value() != other.__value()
 
    def __add__(self, other: "Money"):
        msum = Money(0,0)
        msum.__set_value(self.__value() + other.__value())
        return msum
 
    def __sub__(self, other: "Money"):
        difference = self.__value() - other.__value()
        if difference < 0:
            raise ValueError("a negative result is not allowed")
        dmoney = Money(0,0)
        dmoney.__set_value(self.__value() - other.__value())
        return dmoney