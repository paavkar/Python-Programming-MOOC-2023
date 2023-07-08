# WRITE YOUR SOLUTION HERE:
class SimpleDate:

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    def __lt__(self, another):
        if(self._year < another._year):
            return True
        elif(self._year <= another._year and self._month < another._month):
            return True
        elif(self._year <= another._year and self._month <= another._month and self._day < another._day):
            return True
        else:
            return False

    def __gt__(self, another):
        if(self._year > another._year):
            return True
        elif(self._year >= another._year and self._month > another._month):
            return True
        elif(self._year >= another._year and self._month >= another._month and self._day > another._day):
            return True
        else:
            return False

    def __eq__(self, another):
        if(self._year == another._year and self._month == another._month and self._day == another._day):
            return True
        else:
            return False

    def __ne__(self, another):
        if(self._year != another._year or self._month != another._month or self._day != another._day):
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"
    
    def __add__(self, increment: int):
        new = SimpleDate(self._day, self._month, self._year)
        if(new._day + increment <= 30):
            new._day += increment
            return new
        if(new._month <= 11 and increment / 30 <= 2):
            if(new._day + increment <= 30):
                new._day = new._day + increment - 30
            else:
                days = increment - 30
                months = increment // 30
                new._month += months
                if(days == 0):
                    new._day = new._day + days
                else:
                    new._month += 1
                    new._day = new._day + days - 30
        else:
            years = increment // 30 // 12
            rest_of_days = years * 30 * 12
            increment = increment - rest_of_days
            new._year += years
            if(increment / 30 < 1 and new._day + increment <= 30):
                new._day += increment
            else:
                months = increment // 30
                if(new._month < 12):
                    new._month += months
                else:
                    new._year += 1
                    new._month = 0
                    new._month += months
                    rest_of_days = months * 30
                    increment = increment - rest_of_days
                    if(new._day + increment <= 30):
                        new._day += increment
                    else:
                        new._month += 1
                        new._day = new._day - 30 + increment
        return new
    

    def __sub__(self, another):
        days_in_year1 = self._day + self._month * 30 + self._year * 30 * 12
        days_in_year2 = another._day + another._month * 30 + another._year * 30 * 12
        return abs(days_in_year1 - days_in_year2)

if __name__ == "__main__":
    sdate = SimpleDate(1, 5, 1878)
    print(sdate + 30)
    sdate = SimpleDate(23, 5, 1999)
    print(sdate + 45)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)


### Example solution
# Comparisons are easier, when date is converted to days
    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__day
 
    # Converst days back to date
    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)
    
    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()
 
    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()
 
    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()
        
    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()
 
    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)
 
    def __sub__(self, other: "SimpleDate"):
        # abs(x) returns the absolute value of x
        return abs(self.__value() - other.__value())
 