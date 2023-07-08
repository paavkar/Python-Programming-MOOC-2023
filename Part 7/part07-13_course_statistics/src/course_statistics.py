# Write your solution here
import json
import urllib.request
def retrieve_all():
    data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courses = data.read()
    courses = json.loads(courses)
    active = []
    for course in courses:
        if(course['enabled'] == True):
            active.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))
    return active


def retrieve_course(course_name: str):
    data = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course = data.read()
    course = json.loads(course)
    returned_course = {}
    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    for index, week in course.items():
        weeks += 1
        if(week["students"] > students):
            students = week["students"]
        hours += week["hour_total"]
        exercises += week["exercise_total"]
    returned_course["weeks"] = weeks
    returned_course["students"] = students
    returned_course["hours"] = hours
    returned_course["hours_average"] = hours//students
    returned_course["exercises"] = exercises
    returned_course["exercises_average"] = exercises//students
    return returned_course