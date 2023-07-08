# Write your solution here
from datetime import datetime
def is_it_valid(pic: str):
    if(len(pic) != 11):
        return False
    controls = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    day = pic[:2]
    month = pic[2:4]
    year = pic[4:6]
    marker = pic[6:7]
    control = pic[-1]
    control_check = int(day+month+year+pic[7:-1]) % 31
    if(controls[control_check] != control):
        return False
    if(marker == "+"):
        year = "18" + year
    elif(marker == "-"):
        year = "19" + year
    elif(marker == "A"):
        year = "20" + year
    try:
        birthday = datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    if(marker != "+" and marker != "-" and marker != "A"):
        return False
    return True

### Example Solution

from datetime import datetime
 
def is_it_valid(pic: str):
    if len(pic) != 11:
        return False
    numbers = pic[:6]+pic[7:10]
    for x in numbers:
        if x not in "0123456789":
            return False
    century_marker = pic[6]
    if century_marker not in "+-A":
        return False
    day = int(pic[:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    if century_marker == "+":
        year += 1800
    if century_marker == "-":
        year += 1900
    if century_marker == "A":
        year += 2000
    try:
        test = datetime(year, month, day)
    except:
        return False
    characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
    index = int(numbers)%31
    return characters[index] == pic[-1]