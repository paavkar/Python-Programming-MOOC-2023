# Write your solution here
import csv
from datetime import datetime
def cheaters1():
    cheater_list = []
    start_times = []
    submissions = []
    with open("start_times.csv") as start:
        for line in csv.reader(start, delimiter=";"):
            start_times.append(line)
    with open("submissions.csv") as start:
        for line in csv.reader(start, delimiter=";"):
            submissions.append(line)
    for submission in submissions:
        submission[3] = datetime.strptime(submission[3], "%H:%M")
    for person in start_times:
        person[1] = datetime.strptime(person[1], "%H:%M")
        for submission in submissions:
            if person[0] == submission[0]:
                delta = submission[3] - person[1]
                delta = delta.seconds/60/60
                if(delta > 3):
                    if(person[0] not in cheater_list):
                        cheater_list.append(person[0])
    return cheater_list

### Example solution

import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
 
        return cheaters
 
# Write your solution here