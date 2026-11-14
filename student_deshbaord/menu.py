from signup.sign import students,Teacher
from login.login import login




def menu():
    while True:
        print("--------------DESHBOARD-------------------")
        print("1.student_registration")
        print("2.teacher_registration")
        print("3.login")
        print("4.exit")
        choice=input("please enter the choice: ")
        if choice=="1":
            ob=students()
            ob.reg()
        elif choice=="2":
            ob=Teacher()
            ob.reg()
        elif choice=="3":
            ob=login()
            ob.login()
        elif choice=="4":
            print("exit")
            break
        else:
            print("sorry please try agin:")
            break

menu()            
        
                
    
    