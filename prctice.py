students = []

while True:

    student = {}

    student["name"] = input("Enter student name: ")

    n = int(input("How many subjects do you have? "))

    subjects = []
    
    total_marks = 0
    obtained_marks = 0

    for i in range(n):

        sub = {}

        sub["subject_name"] = input("Enter subject name: ")

        sub["total"] = int(input("Enter total marks: "))
            

        sub["marks"] = int(input("Enter obtained marks: "))

        total_marks += sub["total"]

        obtained_marks += sub["marks"]
        subjects.append(sub)

    student["subjects"] = subjects

    student["total_marks"] = total_marks

    student["obtained_marks"] = obtained_marks

    student["percentage"] = (total_marks /obtained_marks ) * 100
    

    students.append(student)

    choice = input("Do you want to add another student? (yes/no): ")

    if choice.lower() != "yes":
        break


print("\n========== ALL STUDENTS DATA ==========")

for student in students:

    print("\nStudent Name:", student["name"])

    print("Subjects:", student["subjects"])

    print("Total Marks:", student["total_marks"])

    print("Obtained Marks:", student["obtained_marks"])

    print("Percentage:", student["percentage"])
    if sub["total"] <=33:
        print(f"you are fail in {sub["subject_name"]}")
    else:
        print(f"you are pass in {sub["subject_name"]}")    