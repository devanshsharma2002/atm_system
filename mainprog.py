class Atm:
    def __init__(self):
        self.pin=0
        self.balance=int(0)
        
        self.menu()

    def menu(self):
        user_input=1
        while user_input in range(1,5) : 
            user_input= int(input("""
    Hello how would you like to proceed?
    1->Generate pin
    2->Deposit 
    3->Withdrw
    4->Check balance
    5->EXIT
    -->"""))
            if user_input==1:
                print('GENERATE PIN !')
                self.pin_gen()

            elif user_input==2:
                print('DEPOSIT ')
                self.balance=self.deposit()
                

            elif user_input==3:
                print('WITHRAW')
                self.balance=self.withdraw()
                
            elif user_input==4:
                print('BALANCE CHECK')
                self.bal_chk()

            elif user_input==5:
                print('EXIT!')
            
            elif user_input not in range(1,6):
                print('Invalid Input , Please Enter Valid Option Referring to The Options presented !')
                user_input=1
        
        
    def pin_gen(self):
        self.pin=int(input('Please enter the pin : '))
    
    def deposit(self):
        if (int(input('Enter your PIN : '))== self.pin):
            dep_amt=int(input('Enter The Amount To be Deposited : '))
            print(f'Current Bal :{self.balance+dep_amt}')
            return self.balance+dep_amt
        else:
            print('Wrong Pin !!!')
            return self.balance
    
    def withdraw(self):
        if (int(input('Enter your PIN : '))== self.pin):
            with_amt=int(input('Enter The Amount To be Withdrawn : '))
            print(f'Current Bal :{self.balance-with_amt}')
            return self.balance-with_amt
        else:
            print('Wrong Pin !!!')
            return self.balance
        
    def bal_chk(self):
        if (int(input('Enter your PIN : '))== self.pin):
            print(f'balance : { self.balance}')
        else:
            print('Wrong Pin !!! Try Again ')
        



        

#main
a=Atm()