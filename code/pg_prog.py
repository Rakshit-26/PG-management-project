#PROJECT DETAILS
#COMPUTER CLASS XII PROJECT
#TOPIC: PG MANAGEMENT
#BY: RAKSHIT AGRAWAL(No Project Partner)
#    XII B
import price
import layout
import caretaker
import guests
import mysql.connector as ms
from getpass import getpass
mycon=ms.connect(host='localhost', user='root', passwd='rakshit',charset='utf8', database='PG')
mycursor=mycon.cursor()
#Details of ROOMS already in SQL Database
#PG has Ground and 3 extra floors
#ONE_MONTH_BEFORE_DUE_DATE column denotes the date that is one month prior to due date.
#Residents must pay the rent of the month before staying for that month.
print("\t\t\t\t", 27*"**")
print("\t\t\t\t\t      WELCOME TO COSMIC BOYS PG")
print("\t\t\t\t", 27*"**")
print("\n#FOOD & AMENITIES:\n We offer you a clean, hygienic, spacious and secure accommodation along with the following amenities:\n\n")
print("    Air conditioner                  Internet                  Kitchen                  2-Wheeler Parking\n\n\
    24hrs Hot Water                   CCTV                     Security           Food Facility [No extra charges]")
print("\n\n#ROOMS:\n Wide variety of well ventilated and clean rooms, offering full privacy are:")
print("\n    1P Rooms: Single occupancy rooms[", end="")
print(price.r_price1p(), end="")
print("]")
print("\n    2P Rooms: Double occupancy rooms[", end="")
print(price.r_price2p(), end="")
print("]")
print(60*"__")
print("\n RENT PAYMENT POLICY: 1.Security deposit is 1 month rent \n                      2.Rent must be paid monthly \n                      3.All payments are non-refundable")
print(60*"__")
print("\n", end="")
enter=input("Press ENTER to continue...\n")
#
#MAIN PROGRAM IS DIVIDED INTO TWO PARTS
#
def part1():                                                        #For user as guest
    print("Choose from the following options to get to know about:")
    print("1.FLOORWISE LAYOUT of PG")
    print("2.Details of all rooms")
    print("3.Details of unoccupied rooms w.r.t. the room type")
    print("4.Details of unoccupied rooms w.r.t. the floor")
    cho=int(input("Enter your choice(1/2/3/4)=>"))
    if cho==1:                                                      #floorwise layout
        layout.pgmap()
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Administrator:")
            user=input("USERNAME:")                          #USERNAME:rakshit
            password=getpass("PASSWORD:")                    #PASSWORD:rakshit
            if user=="rakshit" and password=="rakshit":
                part2()
            else:
                print("INVALID INPUT")
                print("Username and password do not match.")
        elif goal==2:
            part1()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif cho==2:                                                    #all rooms' details
        guests.t_rooms(mycursor)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Administrator:")
            user=input("USERNAME:")                          #USERNAME:rakshit
            password=getpass("PASSWORD:")                    #PASSWORD:rakshit
            if user=="rakshit" and password=="rakshit":
                part2()
            else:
                print("INVALID INPUT")
                print("Username and password do not match.")
        elif goal==2:
            part1()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif cho==3:                                                    #unocc. rooms(typewise)
        print("Choose from the following options to get to know about:")
        print("1.Details of all unoccupied rooms")
        print("2.Details of all 1P unoccupied rooms")
        print("3.Details of all 2P unoccupied rooms")
        choi=int(input("Enter your choice(1/2/3)=>"))
        if choi==1:                                                 #all unocc. rooms
            guests.unocc_rooms(mycursor)
            print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]") #switch user
            goal=int(input("Enter your choice(1/2/3)=>"))
            if goal==1:
                print("\nLogging in as Administrator:")
                user=input("USERNAME:")                      #USERNAME:rakshit
                password=getpass("PASSWORD:")                #PASSWORD:rakshit
                if user=="rakshit" and password=="rakshit":
                    part2()
                else:
                    print("INVALID INPUT")
                    print("Username and password do not match.")
            elif goal==2:
                part1()
            elif goal==3:
                print("\t\t\t\t\t\t---THANKYOU---")
            else:
                print("INVALID INPUT")
        elif choi==2:                                               #all unocc. 1P rooms
            guests.unocc_1prooms(mycursor)
            print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]") #switch user
            goal=int(input("Enter your choice(1/2/3)=>"))
            if goal==1:
                print("\nLogging in as Administrator:")
                user=input("USERNAME:")                      #USERNAME:rakshit
                password=getpass("PASSWORD:")                #PASSWORD:rakshit
                if user=="rakshit" and password=="rakshit":
                    part2()
                else:
                    print("INVALID INPUT")
                    print("Username and password do not match.")
            elif goal==2:
                part1()
            elif goal==3:
                print("\t\t\t\t\t\t---THANKYOU---")
            else:
                print("INVALID INPUT")
        elif choi==3:                                               #all unocc. 2P rooms
            guests.unocc_2prooms(mycursor)
            print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]") #switch user
            goal=int(input("Enter your choice(1/2/3)=>"))
            if goal==1:
                print("\nLogging in as Administrator:")
                user=input("USERNAME:")                      #USERNAME:rakshit
                password=getpass("PASSWORD:")                #PASSWORD:rakshit
                if user=="rakshit" and password=="rakshit":
                    part2()
                else:
                    print("INVALID INPUT")
                    print("Username and password do not match.")
            elif goal==2:
                part1()
            elif goal==3:
                print("\t\t\t\t\t\t---THANKYOU---")
            else:
                print("INVALID INPUT")
    elif cho==4:                                                    #unocc. rooms(floorwise)
        x=int(input("Please specify the floor whose rooms' details you want to know(0/1/2/3):"))
        if x in (0,1,2,3):
            if x==0:
                y="GROUND"
            elif x==1:
                y="FIRST"
            elif x==2:
                y="SECOND"
            elif x==3:
                y="THIRD"
            guests.F0_rooms(mycursor, y)
            print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]") #switch user
            goal=int(input("Enter your choice(1/2/3)=>"))
            if goal==1:
                print("\nLogging in as Administrator:")
                user=input("USERNAME:")                      #USERNAME:rakshit
                password=getpass("PASSWORD:")                #PASSWORD:rakshit
                if user=="rakshit" and password=="rakshit":
                    part2()
                else:
                    print("INVALID INPUT")
                    print("Username and password do not match.")
            elif goal==2:
                part1()
            elif goal==3:
                print("\t\t\t\t\t\t---THANKYOU---")
            else:
                print("INVALID INPUT")
        else:
            print("INVALID INPUT")
    else:
        print("INVALID INPUT")

def part2():                                                        #For user as administrator
    print("Choose from the following options to:")
    print("1.Get Details of all residents")
    print("2.Add details of a new resident")
    print("3.Remove details of a resident")
    print("4.Get Details of all residents with pending dues(for >=1 month)")
    print("5.Clear dues of a resident")
    print("6.Get Details of all residents availing food facility")
    print("7.Change food requirement of a resident")
    print("8.Change rooms' rent")
    choice=int(input("Enter your choice(1/2/3/4/5/6/7/8)=>"))
    if choice==1:                                                   #residents' details
        caretaker.t_residents(mycursor)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==2:                                                 #add resident
        caretaker.new_res(mycursor, mycon)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==3:                                                 #remove resident
        caretaker.remove_res(mycursor, mycon)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==4:                                                 #rent defaulters
        caretaker.dues(mycursor, mycon)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==5:                                                 #clear dues
        caretaker.clear_dues(mycursor, mycon)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==6:                                                 #residents availing food facility
        caretaker.food_residents(mycursor)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==7:                                                 #change food req.
        caretaker.ch_food(mycursor, mycon)
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    elif choice==8:                                                 #change rent
        price.ch_rent()
        print("\n\nPress[1 to SWITCH USER], [2 for BACK TO MENU], [3 for EXIT]")     #switch user
        goal=int(input("Enter your choice(1/2/3)=>"))
        if goal==1:
            print("\nLogging in as Guest:")
            part1()
        elif goal==2:
            part2()
        elif goal==3:
            print("\t\t\t\t\t\t---THANKYOU---")
        else:
            print("INVALID INPUT")
    else:
        print("INVALID INPUT")

#
#NOTE: Guest is only given rights to access details of unoccupied rooms by security point of view 
#
#ALL THE MODULES AND FUNCTIONS ARE COMBINED IN THE FOLLOWING PROGRAM
y=""
print("Login as:  1.Guest \n           2.Administrator\n")
ch=int(input("Enter your choice(1/2)=>"))
if ch==1:
    part1()
elif ch==2:
    user=input("USERNAME:")                                  #USERNAME:rakshit
    password=getpass("PASSWORD:")                            #PASSWORD:rakshit
    if user=="rakshit" and password=="rakshit":
        part2()
    else:
        print("INVALID INPUT")
        print("Username and password do not match.")
else:
    print("INVALID INPUT")

mycon.close()

