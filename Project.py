import sys


def grades(grade):
    if grade>90:
        temp = 'AA'
        return temp
    if grade<90 and grade>70:
        temp = 'BB'
        return temp
    if grade<70 and grade>50:
        temp = 'CC'
        return temp
    if grade<50 and grade>30:
        temp = 'DD'
        return temp
    else:
        temp = 'FF'
        return temp

def course_percentage():
    midterm = int(input("Enter your midterm score: "))
    project = int(input("Enter your project score: "))
    final = int(input("Enter your final score: "))
    dict = {}
    dict["midterm"] = midterm
    dict["final"] = final
    dict["project"] = project
    grade = dict["midterm"] * 30/100 + dict["final"] * 50/100 + dict["project"] *20/100
    if grade > 90: print("Your score is AA")
    if grade < 90 and grade > 70: print("Your score is BB")
    if grade < 70 and grade > 50: print("Your Score is CC")
    if grade < 50 and grade > 30: print("Your score is DD")
    if grade < 30: print("Your score is FF. {} {} failed.".format(name,surname))


#student login part
print("You have 3 attempts to login")
i=1
while i<4:
    name, surname = input("Please enter your name: ").split()
    if name == "Berilcan" and surname=="Kutlu":
        print("Welcome {} {} !".format(name,surname))
        break
    else:
        print("Try again! {} attempt left".format(3-i))
        i=i+1
        if i==4:
            print("Please try again later!")
            sys.exit()

courses = []
num_course = int(input("Have many courses will you choose?"))
for i in range(0,num_course):
    course = input("Enter your course name: ")
    courses.append(course)
choosen_course = input("You must choose a course to have an exam: ")
if choosen_course in courses:
    letter_grade = (course_percentage())
else:
    print("The course is not in the list. Login again.")
    sys.exit()

