# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if(self.seconds < 59):
            self.seconds += 1
        else:
            if(self.minutes < 59):
                self.minutes += 1
                self.seconds = 0
            else:
                self.minutes = 0
                self.seconds = 0
    
    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"
    
### Example solution
def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0