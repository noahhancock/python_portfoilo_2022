#Noah Hancock
#Guess my number game
#10/28/19

#imports
import random


#functions
def check(rmin, rmax):
    while True:
        num= input("please pick a  number between " +str(rmin) +" and "+str(rmax)+"\n")
        if num.isdigit():
            num= int(num)
            if num >= rmin and num <= rmax:
                return num
        print("not a good value")

    



#set up program optoins
rmin=1
rmax=10
max_trys= 3

def menu():
    while True:
        print("""
    Welcome to guess the number game.
    press 1 for options,
    press 2 to play the game,
    press 3 to quit,
    press 4 to play with the computer""")
        choice=input("Please enter your choice here.\n")
        if choice=="1":
            options()
        elif choice=="2":
            guess_my_num(rmin,rmax,max_trys)
        elif choice=="3":
            x= confirm()
            if x == True:
                quit()
        elif choice =="4":
            computer()

def computer():
    num= input("please pick a number for your min\n")
            if num.isdigit():
                num= int(num)
                rmin = num
                rmin=num
    ber= input("please pick a number for your max\n")
            if ber.isdigit():
                ber= int(ber)
                rmax=ber
    numb= input("please pick a number for how many tries the computer has\n")
            if numb.isdigit():
                numb= int(numb)
                max_trys=numb
    while True:
        randnum= random.randint(gmin,gmax)
        print("is the number",randnum)
        response= input("please tell the computer if your number is lower or higher then your number\n")
        if "lower" in response:
            gmin= randnum
            
        elif "higher" in response:
            

def confirm():
    while True:
        confirm=input("are your sure\n")
        if "y" in confirm:
            return True
        elif "n" in confirm:
            return False

    
def options():
    global rmin
    global rmax
    global max_trys
    while True:
        print("""
please pick a difficulty
easy press 1
medium press 2
hard press 3
custom press 4
""")
        choice= input(" pick your option\n")
        if choice=="1":
            rmin=1
            rmax=5
            max_trys=3
        elif choice=="2":
            rmin=1
            rmax=10
            max_trys=3
        elif choice=="3":
            rmin=1
            rmax=100
            max_trys=10
        elif choice=="4":
            num= input("please pick a number for your min\n")
            if num.isdigit():
                num= int(num)
                rmin = num
                rmin=num
            ber= input("please pick a number for your max\n")
            if ber.isdigit():
                ber= int(ber)
                rmax=ber
            numb= input("please pick a number for how many tries you have\n")
            if numb.isdigit():
                numb= int(numb)
                max_trys=numb
        break
    menu()
            
            
        


#start game
def guess_my_num(rmin,rmax,max_trys):
    randnum= random.randint(rmin,rmax)
    guess= check(rmin,rmax)
    trys= 0
    trys+= 1
    while guess != randnum and trys != max_trys:
        if guess > randnum:
            print("guess lower")
        else:
            print("guess higher")
        guess= check(rmin,rmax)
        trys+= 1
    #end game loop
    if guess== randnum:
        print("winner")
    else:
        print("loser")
        print("number was", randnum)
        

menu()
