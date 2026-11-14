import json

with open("task.json","r") as file:
    data=json.load(file)

def add_new_contect():
    while True:
        name = input("please enter the name: ")
        subject_name= int(input("How many subjects do you have? "))
        total_marks = 0
        obtained_marks = 0

        subject_name  = input("Enter subject name: ")

        total= int(input("Enter total marks: "))

        marks = int(input("Enter obtained marks: "))

        total_marks += total

        obtained_marks += marks
        percentage = (obtained_marks / total_marks) * 100
        
        dictionary={
            "name":name,
            "subject":subject_name,
            "total_marks":total,
            "obatained": obtained_marks,
            "percentage":percentage
        }
    
        data.append(dictionary)
        with open("task.json","w") as file:
            json.dump(data,file,indent=4)
        print("data save succesfully")
        choice = input("Do you want to add another student? (yes/no): ")

        if choice.lower() != "yes":
            break


        print("\n========== ALL STUDENTS DATA ==========")
        print("\nStudent Name   :", name)
        print("Subjects         :", subject_name)
        print("Total Marks      :",  total)
        print("Obtained Marks   :", obtained_marks)
        print("Percentage       :", percentage)      
                
            
add_new_contect()            