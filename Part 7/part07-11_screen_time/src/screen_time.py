# Write your solution here
from datetime import datetime, timedelta
filename = input("Filename: ")
starting = input("Starting date: ")
starting_date = datetime.strptime(starting, "%d.%m.%Y")
day = int(input("How many days: "))
day_count = day
end_date = starting_date+timedelta(days=day_count-1)
end_date = end_date.strftime("%d.%m.%Y")
print("Please type in screen time in minutes on each day (TV computer mobile):")
times = []
i = 0
while day_count > 0:
    days_added = timedelta(days=i)
    date = starting_date+days_added
    date = date.strftime("%d.%m.%Y")
    screen_time = input(f"Screen time {date}: ")
    times.append(screen_time)
    day_count -= 1
    i += 1
total_time = 0
for time in times:
    index = time.find(" ")
    total_time += int(time[:index])
    time = time[index+1:]
    index = time.find(" ")
    total_time += int(time[:index])
    time = time[index+1:]
    total_time += int(time)
with open(filename, "w") as file:
    date = starting_date.strftime("%d.%m.%Y")
    file.write(f"Time period: {date}-{end_date}\n")
    file.write(f"Total minutes: {total_time}\n")
    file.write(f"Average minutes: {total_time/day}\n")
    i = 0
    for time in times:
        time = time.replace(" ", "/")
        days_added = timedelta(days=i)
        date = starting_date+days_added
        date = date.strftime("%d.%m.%Y")
        file.write(f"{date}: {time}\n")
        i += 1
    
print(f"Data stored in file {filename}")

### Example Solution
from datetime import datetime, timedelta
 
week = timedelta(days=7)
 
def format(aika):
    return aika.strftime("%d.%m.%Y")
 
file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )
 
with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {file}")
# Write your solution here