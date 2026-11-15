
from abc import ABC, abstractmethod
users=[]
class reg(ABC):

    @abstractmethod
    def reg(self):
        pass

    @abstractmethod
    def show(self):
        pass 
    
class Student(reg):
    def reg(self):
        while True:
            self.name = input("please enter the name:")
            if len(self.name)>4:
                if self.name.isalpha():
                    break
                else:
                    print("Invalid Your Name")
            else:
                print("Invalid Your Name")
        while True:
            self.age = input("please enter the age:")
            if len(self.age)>0:
                if self.age.isdigit():
                    break
                else:
                    print("Invalid Your Age")
            else:
                print("Please Age 0 to Greater")
        while True:
                     
            self.address=input("Enter Address: ")
            if len(self.address)>4:
                if self.address.isalpha():
                    break
                else:
                    print("Invalid Your Address")
            print("Invalid Your Address")
        while True:
            self.email=input("Enter Email ID: ")
            if len(self.email)>6:
                if "@" in self.email and ".com" in self.email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                print("Invalid Your Email ID")   
                
        while True:
            self.password=input("Enter Password: ")
            if len(self.password)>6:
                if self.password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
            else:
                print("Please 6 character password try again")                        

        users.append(self)
        print("Student Registration Successful!")
    def show(self):
        print("name:",self.name)
        print("age",self.age)
        print("email",self.email) 
        print("password",self.password)   
        
        
        # print(users)
        
class Teacher(reg):
    
    def reg(self):
        
        while True:
            self.name = input("please enter the name:")
            if len(self.name)>4:
                if self.name.isalpha():
                    break
                else:
                    print("Invalid Your Name")
            else:
                print("Invalid Your Name")
        while True:
            self.age = input("please enter the age:")
            if len(self.age)>0:
                if self.age.isdigit():
                    break
                else:
                    print("Invalid Your Age")
            else:
                print("Please Age 0 to Greater")
        while True:
                     
            self.address=input("Enter Address: ")
            if len(self.address) > 4:
                    
                if self.address.isalpha():
             
                    break
                else:
                    print("Invalid Your Address")
            print("Invalid Your Address")
        while True:
            self.email=input("Enter Email ID: ")
            if len(self.email)>6:
                if "@" in self.email and ".com" in self.email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                print("Invalid Your Email ID")   
                
        while True:
            self.password=input("Enter Password: ")
            if len(self.password)>6:
                if self.password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
            else:
                print("Please 6 character password try again")
        users.append(self)
        print("teacher  Registration Successful!")
        # print(users)
class Login():

    def log(self):
        print("\n****** LOGIN PAGE ******")

        self.email = input("Please enter the email: ")
        self.password = input("Please enter the password: ")

        for i in users:

            if i.email == self.email:

                if i.password == self.password:

                    print("\nLogin Successfully!")

                    print("Name:", i.name)
                    print("Age:", i.age)
                    print("Address:", i.address)
                    print("Email:", i.email)

                    if isinstance(i, Student):
                        print("Role: Student")

                    elif isinstance(i, Teacher):
                        print("Role: Teacher")

                    return

                else:
                    print("Invalid Password!")
                    return

        print("Data Is Not Registered!")

        
def menu(): 
    while True:
    
            print("\n================================")
            print("       REGISTRATION SYSTEM")
            print("================================")
    
            print("1. Student Registration")
            print("2. Teacher Registration")
            print("3. Login")
            print("4. Exit")
    
            choice = input("Enter Your Choice: ")
    
            if choice == "1":
    
                obj = Student()
                obj.reg()
    
            elif choice == "2":
    
                obj = Teacher()
                obj.reg()
    
            elif choice == "3":
    
                obj = Login()
                obj.log()
    
            elif choice == "4":
    
                print("Thank You!")
                break
    
            else:
    
                print("Invalid Choice!")

menu()   
        
    
