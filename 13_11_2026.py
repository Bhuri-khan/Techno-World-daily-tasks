class Bank:
    def __init__(self):
        # Public variables
        self.bankname = "SBI"
        # Protected variables
        self._accountholdername = "Bhuri"
        # Private variables
        self.__accountnumber = 12345678
        self.__accountbalance = 20000
    def balance(self):
        print("Account Balance:", self.__accountbalance)
    def Deposit(self):

        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            self.__accountbalance += amount
            print("Amount deposited successfully!")
            print("Remaining Balance:", self.__accountbalance)
        else:
            print("Invalid amount")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount")

        elif amount <= self.__accountbalance:
            self.__accountbalance -= amount
            print("Withdraw successful!")
            print("Remaining Balance:", self.__accountbalance)

        else:
            print("Insufficient Balance!")
    def update(self):
        print("1. Update Account Holder Name")
        print("2. Update Account Number")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self._accountholdername = input("Enter new name: ")
            print("Name updated successfully!")
        elif choice == 2:
            self.__accountnumber = int(input("Enter new account number: "))
            print("Account number updated successfully!")
        else:
            print("Invalid choice")
class Bank2(Bank):

    def __init__(self):
        super().__init__()

    def show_data(self):
        print("Bank Name:", self.bankname )
        print("Account Holder Name:", self._accountholdername)
        self.balance()


        
ob = Bank2()
ob.show_data()
ob.Deposit()
ob.withdraw()
ob.update()