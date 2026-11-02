# import random
# secret_number = random.randint(1,100)

# attempt=0
# while True:
#     attempt+=1
#     number = int(input("please enter the number:"))
#     if number==secret_number:
#         print(f"thankyou your number is correct: {attempt}")
#         break
        
#     elif number > secret_number:
#         print("too high please try number:")
        
#     elif number < secret_number:
#         print("too low please enter the number")
           
#     else:
#         print("try")
#         break

import random
secret_number=random.randint(1,100)



def func():
    attempt=0
    count=0 
    print("your attempt is start only 5 attempt: ")
    for i in range(5):
         
        attempt+=1
        count = 5 - attempt
        number=int(input("please enter the number:"))
        if number == secret_number:
            print(f"thankyou your number is carrect: {secret_number},attempt{attempt}")
            break
    
        elif number > secret_number:
            print(f"too high please enter the number:{count}")
        elif number < secret_number:
            print(f"too low please enter the number:{count}")
        else:
            print(f"sorry   your attempt is {attempt}: your secret number is:{secret_number}")
            break                 
func()        
while True:
    choice = input("Do you want play again: (yes/no)")
        
    if choice == "yes":
        func()
    elif choice=="no":
        print("thank you ")    
        break
