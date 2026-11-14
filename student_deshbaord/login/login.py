
import json
class login():
    def login(self):
        

        try:
            
            self.email=input("please enter the email:")
            self.password=input("please enter the password:")
            with open("task.json","r") as file:
                self.data=json.load(file)
            for i in self.data:    
                if i["email"]==self.email and i["password"]==self.password:
                    print("login succesfully") 
                    return       
            
                else:
                    print("email or password not match:")
                    break
        except Exception as e:
            print("error is ",e)    
            

            
