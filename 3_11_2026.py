import json
import datetime
with open("data.json","r") as file:
    data=json.load(file)

def add_new_contect():
    dictionary={} 
    while True:
            name = input("please enter the name:")
            if len(name)>2:
                if name.isalpha():
                    break
                    
                else:
                    with open("errors.log",'a') as file_name:
                        file_name.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name - invalid your name \n")
                    print("Invalid Your Name")
            else:
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - Name -  Minimum 2 Character \n")
                print("Invalid Name")

       
    
    while True:
            email=input("Enter Email ID: ")
            if len(email)>6:
                if "@" in email and ".com" in email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - email - Invalid Your    Email \n")
                print("Invalid email")
         
            
            
    while True:
            number=input("Enter number: ")
            if len(number)<11:
                if number.isalnum():
                    break
                else:
                    print("Invalid Your number")
            else:
                print("Please 10 character number  try again")
                
                with open("errors.log",'a') as file:
                    file.write(f"[{str(datetime.datetime.now())}] [ERROR] - password - Invalid Your Password \n")
                print("Invalid number")
        
    dictionary={
        "name":name,
        "email":email,
        "number":number
   
}
    with open("data.json","w") as file:
        data.append(dictionary)
        json.dump(data,file,indent=4)
    print("data save succesfully")
     
def view_contect():
        with open("data.json","r") as file:
            data=file.read()
            print(data)
        print("thankyou")

def search():
    with open("data.json","r")as file:
        data=json.load(file)
    name = input("please enter the name:") 
    for i in data:

        if i["name"].lower() == name.lower():
            print("Name: ",i["name"])
            print("Email: ",i["email"])
            print("number:" ,i["number"])
            return
        else:        
    
            print("data is not found")
            break
    else:
        print("please enter the add data student:")     
  
def update():
    with open("data.json","r+") as file:
        data=json.load(file)
    
    while True:
            
        print("1.update_name")
        print("2.update_email")
        print("3.update_number")
        print("4.exit")
        choice=int(input("please enter the choice : "))
        if choice==1:
            name1=input("enter corrent name : ")
            name2=input("enter new name : ")
                
            for i in data:
                if i["name"]==name1:
                    i["name"]=name2
                with open("data.json","w") as file:
                    json.dump(data,file,indent=4)

                print("save name successfully")
                    
            
        if choice==2:
            email1=input("enter corrent name : ")
            email2=input("enter new name : ")
                
            for i in data:
                if i["email"]==email1:
                    i["email"]=email2
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)
        
            print("email update successfully")    
            
        if choice==3:
            number1=input("enter corrent name : ")
            number2=input("enter new name : ")
                       
            for i in data:
                if i["number"]==number1:
                    i["number"]=number2
            with open("data.json","w") as file:
                json.dump(data,file,indent=4)
               
            print("number update successfully")        
        else:
            print("data not match and data is not found:")
    
def delete():
    
    with open("data.json", "r") as file:
        data = json.load(file)

        name = input("Please enter the name to delete: ")

    for i in data:
        if i["name"].lower() == name.lower():
            data.remove(i)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

        print("Contact deleted successfully!")
        return

    print("Data is not found") 
    
  
  
def menu():
    while True:
        print("1.add new contact")
        print("2.view contact")
        print("3.search new contact")  
        print("4.update contect")
        print("5.delete contact")
        print("6.exit")  
        
        choice = int(input("please enter the choice:  "))
        if choice ==1:
            add_new_contect()
        elif choice==2:
            view_contect()
        elif choice==3: 
            search() 
        elif choice==4:
            update()
        elif choice==5:
            delete()
        elif choice==6:
            print("exit")
            break
        else:
            print("thank you")    
            break                          
menu()                                      