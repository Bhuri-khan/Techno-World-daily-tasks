from abc import ABC,abstractmethod
import json
import uuid
import datetime



try:
    with open("student_deshbaord/data/student.json", "r") as file:
        data = json.load(file)

except FileNotFoundError:
    data = []


class reg(ABC):
    @abstractmethod
    def reg(self):
        pass


class students(reg):
    def reg(self):
        print("----start student registration---")
        while True:
            self.name=input("enter your name : ")
            if len(self.name)>=3 and self.name.isalpha():
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid name - {self.name}\n")
                print("invalid name")

        
        self.uuid = uuid.uuid4().hex[:4]
        
        while True:
            self.age=input("enter your age : ")
            if len(self.age)>0 and self.age.isdigit():
                break        
            else:
                
        
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid age - {self.age}\n")
                print("not exist age")            
    
        while True:
            self.email=input("enter your email : ")
            if "@"  in self.email and  self.email.endswith(".com"):
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid email - {self.email}\n")
                print("invalid amail")         
        while True:
            self.password=input("enter your password : ")
            if len(self.password)>=4 and self.password.isdigit():
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid password - {self.password}\n")
                print        
                
                

        print("----registration---") 
        
        date_time=datetime.datetime.now()
        dictionary={
            "uid":self.uuid_data,
            "name":self.name,
            "age":self.age,
            "email":self.email,
            "password":self.password,
            "date_time":str(date_time)
        }
        data.append(dictionary)
        with open("student_deshbaord/student.json", "w") as file:
            json.dump(data, file, indent=4)

        
        print("students successfully registration ")        
class Teacher(reg):
    def reg(self):
        print("----start teacher registration---")
        while True:
            self.name=input("enter your name : ")
            if len(self.name)>=3 and self.name.isalpha():
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid name - {self.name}\n")
                print("invalid name")

        
        self.uuid = uuid.uuid4().hex[:4]
        
        while True:
            self.age=input("enter your age : ")
            if len(self.age)>0 and self.age.isdigit():
                break        
            else:
                
        
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid age - {self.age}\n")
                print("not exist age")            
    
        while True:
            self.email=input("enter your email : ")
            if "@"  in self.email and  self.email.endswith(".com"):
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid email - {self.email}\n")
                print("invalid amail")         
        while True:
            self.password=input("enter your password : ")
            if len(self.password)>=4 and self.password.isdigit():
                break
            else:
                with open("student_deshbaord/loggs/error.py", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid password - {self.password}\n")
                print                        
        print("----registration---") 
                
        date_time=datetime.datetime.now()
        dictionary={
            "uid":self.uuid_data,
            "name":self.name,
            "age":self.age,
            "email":self.email,
            "password":self.password,
            "date_time":str(date_time)
        
        }
        data.append(dictionary)
        with open("student_deshbaord/teacher.json", "w") as file:
            json.dump(data, file, indent=4)

        
        print("teacher successfully registration ")             
        
        