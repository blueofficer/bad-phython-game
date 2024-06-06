import os

print ("welcome to to the game")

clear = lambda: print("\033[2J\033[H", end="", flush=True)# CLEAR FUNCTION

balence = 100
wallet = 50
loggedin = False
correctuser = "admin"
correctpass = "1234"
in_bank = False
in_world = True
bank_name = "bad banking"


while (True == True) : # for game loop
    if (in_world == True and in_bank == True) : #catch in both are true
        in_bank = False
    if (in_world == False and in_bank == False) : #catch if both are false
        in_world = True
    while (in_bank == True): # banking system
        while (loggedin != True):
            print(f"welcome to {bank_name} login")
            username = input("username:")
            password = (input("password:"))
            
            if (username == correctuser and password == correctpass):
                loggedin = True
            else :(print ("username or password is wrong"))
        clear()
        print (f"welcome to {bank_name}.")
        print ("what would you like todo?")
        print ("1: check acount balance")
        print ("2: deposet money")
        print ("3: withdraw money")
        print ("4: change username")
        print ("5: change password")
        print ("6: log out")

        answer = int(input ("opption :"))

        if (answer == 1) : #checks for option 1 witch is acouint balense
            
            input((balence)) #prints balense to console

        elif (answer == 2): #option 2 deposit money

            deposet = input("how much would you like to add? : ")

            if (deposet.isdigit):

                deposet = int(deposet) #turns the string into a int

                if (deposet <= wallet)  :
                    balence = balence + deposet
                    wallet = wallet - deposet
                    input (f"your new balense is {balence} and you have {wallet}$ on hand")

                else: 
                    input(f"sorry not enougf money in your wallet : {wallet} ")

            else :(print ("sorry only numbers allowed")) #if the input is not a number

        elif (answer == 3):
            withdrael = input("how much would you like to withdrawl? : ")
            if (withdrael.isdigit):
                withdrael = int(withdrael)
                if (withdrael > balence):
                    input("sorry not enougf money in the acouint")
                else :

                    balence = balence - withdrael
                    wallet = wallet + withdrael
                    input (f"your new balense is {balence} and you have {wallet}$ on hand")

            else :(print ("sorry only numbers allowed"))

        elif (answer == 4):

            newusername = input("Whats the new username? :")
            correctuser = newusername
            input(f"user name actped new username is : {newusername}"  )

        elif (answer == 5):

            print ("to change password please enter current password")
            password = input("password:")
            
            if(password != correctpass):
                print("sorry password was incorect logging out")
                loggedin = False
            else:
                print ("correct please enter new password")
                newpassword = input ("new password:")
                correctpass = newpassword
        elif (answer == 6):
            loggedin = False
            in_bank = False
            in_world = True
            clear()


    while (in_world == True) :
        answer = input("whare do you wanna go? \n 1:the bank \n 2:the store \n :")
        if (answer.isdigit):
            answer = int(answer)
            if (answer == 1):
                in_world = False
                in_bank = True
                clear()
        
        