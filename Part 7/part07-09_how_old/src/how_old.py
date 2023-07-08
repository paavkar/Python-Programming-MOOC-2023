# Write your solution here
from datetime import datetime
day = input("Day: ")
month = input("Month: ")
year = input("Year: ")

birthday = datetime(int(year), int(month), int(day))
eve = datetime(1999, 12, 31)
delta = eve - birthday
if(delta.days > -1):
    print(f"You were {delta.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")