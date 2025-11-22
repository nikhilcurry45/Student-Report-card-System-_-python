students = []

def add_students():
    print("\n\nAdd new student:")
    roll = int(input("Enter Roll Number:"))
    for student in students:
        if student['roll'] == roll:
            print("Roll number already exist:")
            return
    name = input("Enter name:")

    subjects = {}
    n = int(input("How many Subjects?"))

    for i in range(n):
        sub = input("Enter Subject Name:")
        marks = int(input("Marks (0 - 100)"))
        subjects[sub] = marks
    total = sum(subjects.values())
    percentage = (total / n) 

    if(percentage >= 90):
        grade = 'S'
    elif(percentage >= 80):    
        grade = 'A'
    elif(percentage >= 70):
        grade = 'B'
    elif(percentage >= 60):
        grade = 'C'
    elif(percentage >= 50):
        grade = 'D'
    else:
        grade = 'F'

    student_data = {
        "roll":roll,
        "name":name,
        "subjects":subjects,
        "total":total,
        "percentage":percentage,
        "grade":grade
    }

    students.append(student_data)
    print("Data Added Successfully")

def search_student():
    print("\n\nSearch Student:")
    roll= int(input("enter roll number of student:"))
    for student in students:
        if(student['roll'] == roll):
            print("\n student found:")
            print("Name:",student['name'])
            print("subjects and marks:",student['subjects'])
            print("total:",student['total'])
            print("percentage:",student['percentage'])
            print("grade:",student['grade'])
            return
    print("Student Not Found")


def update_marks():
    print("\n\nUpdate Marks:")
    roll = int(input("enter roll number:"))

    for student in students:
        if(student['roll'] == roll):
            print("Found ",student['name'])
            print("subjects:", list(student["subjects"].keys()))
    
            sub = input("Enter subjects in which marks to be updated:")
        if sub not in student['subjects']:
            print("subject not found:")
            return

        newmarks = int(input("Enter new marks:"))
        student['subjects'][sub] = newmarks

        totsub = student['subjects']
        total = sum(totsub.values())
        percentage = (total / len(totsub)) 
    
        if(percentage >= 90):
            grade = 'S'
        elif(percentage >= 80):    
            grade = 'A'
        elif(percentage >= 70):
            grade = 'B'
        elif(percentage >= 60):
            grade = 'C'
        elif(percentage >= 50):
            grade = 'D'
        else:
            grade = 'F'

        student['total'] = total
        student['percentage'] = percentage
        student['grade'] = grade

        print("Data Updated Successfully")

def show_topper():
    if(students == []):
        print("no data")
        return
    topper = students[0]
    for student in students:
        if(student['percentage'] > topper['percentage']):
            topper = student
    print("\n\nClass topper:")
    print("Name:",topper['name'])
    print("Roll:",topper['roll'])
    print("Subjects",topper['subjects'])
    print("Percentage:",topper['percentage'])
    print("Grade:",topper['grade'])

def display_all():
    if students == []:
        print("no data")
        return
    print("\n\nAll students data:")

    for s in students:
        print("\nName:",s['name'])
        print("Roll:",s['roll'])
        print("Subjects",s['subjects'])
        print("Percentage:",s['percentage'])
        print("Grade:",s['grade'])

while True:
    print("------------------------------------------------------------")
    print("STUDENT REPORT CARD SYSTEM")
    print("1. Add student")
    print("2. Update Marks")
    print("3. Search Student:")
    print("4. Show topper:")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("enter choice:"))
    if(choice == 1):
        add_students()
    elif(choice == 2):
        update_marks()
    elif(choice == 3):
        search_student()
    elif(choice == 4):
        show_topper()
    elif(choice == 5):
        display_all()
    elif(choice == 6):
        break
    else:
        print("Invalid Choice")        
