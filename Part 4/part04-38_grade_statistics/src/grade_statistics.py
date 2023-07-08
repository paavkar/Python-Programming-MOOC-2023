# Write your solution here
def input_from_user():
    grades = []
    points = []
    while True:
        values = input("Exam points and exercises completed: ")
        if(values == ""):
            print_statistics(grades, points)
            break
        personal_points = values.split()
        exercise = int(personal_points[1])//10
        points.append(int(personal_points[0]) + exercise)
        if(int(personal_points[0]) + exercise <= 14 or int(personal_points[0]) < 10):
            grades.append(0)
        elif(int(personal_points[0]) + exercise <= 17):
            grades.append(1)
        elif(int(personal_points[0]) + exercise <= 20):
            grades.append(2)
        elif(int(personal_points[0]) + exercise <= 23):
            grades.append(3)
        elif(int(personal_points[0]) + exercise <= 27):
            grades.append(4)
        elif(int(personal_points[0]) + exercise <= 30):
            grades.append(5)

def print_statistics(grades: list, points: list):
    passes = []
    print("Statistics:")
    print(f"Points average: {sum(points)/len(points)}")
    for grade in grades:
        if(grade > 0):
            passes.append(grade)
    print(f"Pass percentage: {len(passes)/len(grades)*100:.1f}")
    print("Grade distribution:")
    print("  5: " + "*" * grades.count(5))
    print("  4: " + "*" * grades.count(4))
    print("  3: " + "*" * grades.count(3))
    print("  2: " + "*" * grades.count(2))
    print("  1: " + "*" * grades.count(1))
    print("  0: " + "*" * grades.count(0))

input_from_user()

### Example solution
#def exam_and_exercise_completed(inpt):
    #space = inpt.find(" ")
    #exam = int(inpt[:space])
    #exercise = int(inpt[space+1:])
    #return [exam, exercise]
 
#def exercise_points(amount):
    #return amount // 10
 
#def grade(points):
    #boundary = [0, 15, 18, 21, 24, 28]
    #for i in range(5, -1, -1):
        #if points >= boundary[i]:
            #return i
 
#def mean(points):
    #return sum(points) / len(points)
 
#def main():
    #points = []
    #grades = [0] * 6
    #while True:
        #inpt = input("Exam points and exercises completed: ")
        #if len(inpt) == 0:
            #break
 
        #exam_and_exercises = exam_and_exercise_completed(inpt)
        #exercise_pnts = exercise_points(exam_and_exercises[1])
        #total_points = exam_and_exercises[0] + exercise_pnts
 
        #points.append(total_points)
        #grd = grade(total_points)
        #if exam_and_exercises[0] < 10:
            #grd = 0
        #grades[grd] += 1
 
    #pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    #print("Statistics:")
    #print(f"Points average: {mean(points):.1f}")
    #print(f"Pass percentage: {pass_pros:.1f}")
    #print("Grade distribution:")
    #for i in range(5, -1, -1):
        #stars = "*" * grades[i]
        #print(f"  {i}: {stars}")
 
#main()