from datetime import date

def new_res(mycursor, mycon):                               #add resident
    ans="yes"
    while ans=="yes":
        mycursor.execute("Select* from ROOMS where STATUS<>'OCCUPIED'")          #details of all unoccupied rooms
        data=mycursor.fetchall()
        count=mycursor.rowcount
        if count==0:
            print("Sorry!!")
            print("All rooms are occupied")
        else:
            print("Total no. of unoccupied rooms are=", count)
            print("Details of unoccupied rooms are as follows:")
            print("\n\
('ROOM NO.', 'ROOM TYPE', 'FLOOR', 'STATUS')\n")
            for row in data:
                print(row)
            print("\n")                                                          #details of the new resident
            print("Above information might be helpful in proceeding...")
            print("Please enter the following details of the new resident to proceed:")
            name=input("Name:")
            name=name.upper()
            contactno=input("Contact No.(Contact no. of 2 residents mustn't be same):")
            contactno=contactno.strip()
            if len(contactno)==10 and contactno.isdigit():                       #contact no. is a 10 digit number
                dob=input("DOB(YYYY-MM-DD):")
                if dob<=str(date.today()):                                       #dob is not in future
                    add=input("Address:")
                    roomno=input("Room no. alloted:")
                    roomno=roomno.upper()
                    rtype=input("Room type(1P/2P):")
                    rtype=rtype.upper()
                    food=input("Food Requirement(yes/no):")
                    food=food.upper()
                    dues=input("Date upto which payment has been done(YYYY-MM-DD):")
                    if int(dues[5:7])==1:                           #if block to subtract 1 month from due date
                        dues=str(int(dues[0:4])-1)+dues[4]+str(12)+dues[7:] 
                    elif int(dues[5:7]) in (5, 7, 10, 12) and int(dues[8:])==31:
                        dues=dues[0:5]+str(int(dues[5:7])-1)+dues[7]+str(30)
                    elif int(dues[5:7])==3 and int(dues[8:]) in (29, 30, 31):
                        if int(dues[0:4])%4==0 and int(dues[8:])==29:
                            dues=dues[0:5]+str(int(dues[5:7])-1)+dues[7:]
                        elif int(dues[0:4])%4==0 and int(dues[8:]) in (30, 31):
                            dues=dues[0:5]+str(int(dues[5:7])-1)+dues[7]+str(29)
                        else:
                            dues=dues[0:5]+str(int(dues[5:7])-1)+dues[7]+str(28)
                    else:
                        dues=dues[0:5]+str(int(dues[5:7])-1)+dues[7:]
                    stat="Insert into RESIDENTS \
values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format\
(name, contactno, dob, add, roomno, rtype, food, dues)
                    sq="Select* from RESIDENTS where CONTACT_NO='{}'".format(contactno,)
                    mycursor.execute(sq)
                    data=mycursor.fetchall()
                    count=mycursor.rowcount
                    if count==0:            #entered contact no. is unique among residents
                        quer="Select* from ROOMS where ROOM_NO='{}' and R_TYPE='{}'".format(roomno, rtype)
                        mycursor.execute(quer)
                        data=mycursor.fetchall()
                        count=mycursor.rowcount
                        if count==0:
                            print("INVALID INPUT")
                            print("The Room no. and the Room type don't match.")
                        else:               #room exists for given room no. and room type
                            if data[0][3]=="OCCUPIED":
                                print("INVALID INPUT")
                                print("The Room ", roomno, " is already occupied.")
                            else:           #room available
                                if rtype=="1P":
                                    query="Update ROOMS set STATUS='OCCUPIED' where ROOM_NO='{}' and R_TYPE='{}'".format(roomno, rtype)
                                    mycursor.execute(query)
                                    mycon.commit()
                                    print("#ROOM STATUS UPDATED#")
                                else:       #rtype=="2P"
                                    if data[0][3]=="VACANT":
                                        query="Update ROOMS set STATUS='HALF OCCUPIED' where ROOM_NO='{}' and R_TYPE='{}'".format(roomno, rtype)
                                        mycursor.execute(query)
                                        mycon.commit()
                                    else:
                                        query="Update ROOMS set STATUS='OCCUPIED' where ROOM_NO='{}' and R_TYPE='{}'".format(roomno, rtype)
                                        mycursor.execute(query)
                                        mycon.commit()
                                    print("#ROOM STATUS UPDATED#")
                                mycursor.execute(stat)
                                mycon.commit()
                                print("#DATA OF NEW RESIDENT ADDED#")
                    else:
                        print("INVALID INPUT")
                        print("A resident corresponding to the given contact no. already exists.")
                else:
                    print("INVALID INPUT")
                    print("INVALID DOB")
            else:
                print("INVALID INPUT")
                print("Contact no. must be a 10 digit number.")
        ans=input("Want to add data of more residents?(yes/no):")

def t_residents(mycursor):                                  #all residents' details
    mycursor.execute("Select* from RESIDENTS")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("Currently no residents")
    else:
        print("Total no. of residents are=", count)
        print("Details of all the residents are as follows:")
        print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
        for row in data:
            row=list(row)
            row[7]=str(row[7])
            row[2]=str(row[2])
            row=tuple(row)
            print(row)

def remove_res(mycursor, mycon):                            #remove resident
    ans="yes"
    mycursor.execute("Select* from RESIDENTS")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("Currently no residents")
    else:
        while ans=="yes":
            print("Please enter the following details of the resident to delete data:")
            rname=input("Name:")
            rname=rname.upper()
            rcontactno=input("Contact No.:")
            rcontactno=rcontactno.strip()
            if len(rcontactno)==10 and rcontactno.isdigit():                     #contact no. is a 10 digit number
                rroomno=input("Room no.:")
                rroomno=rroomno.upper()
                querys="Select* from RESIDENTS where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(rname, rcontactno, rroomno)
                mycursor.execute(querys)
                data=mycursor.fetchall()
                count=mycursor.rowcount
                if count==0:
                    print("INVALID INPUT")
                    print("The Resident doesn't exist.")
                else:                       #if resident exists
                    print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
                    for row in data:
                        row=list(row)
                        row[7]=str(row[7])
                        row[2]=str(row[2])
                        row=tuple(row)
                        print(row)
                    print("\nAbove information might be helpful in proceeding...\nPLEASE MAKE SURE THAT ALL THE DUES ARE CLEARED BEFORE DELETING THE DATA...")
                    delete=input("Are you sure that you want to delete above resident's data(yes/no):")
                    if delete=="yes":
                        stat="Delete from RESIDENTS where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(rname, rcontactno, rroomno)
                        quer="Select* from ROOMS where ROOM_NO='{}'".format(rroomno,)
                        mycursor.execute(quer)
                        data=mycursor.fetchall()
                        count=mycursor.rowcount
                        if count==0:
                            print("INVALID INPUT")
                            print("The Room corresponding to the given room no. doesn't exist.")
                        else:               #room exists for given room no.
                            if data[0][3]=="VACANT":
                                print("INVALID INPUT")
                                print("The Room ", rroomno, " is already vacant.")
                            else:
                                if data[0][1]=="1P":
                                    query="Update ROOMS set STATUS='VACANT' where ROOM_NO='{}'".format(rroomno,)
                                    mycursor.execute(query)
                                    mycon.commit()
                                    print("#ROOM STATUS UPDATED#")
                                else:       #rtype=="2P"
                                    if data[0][3]=="OCCUPIED":
                                        query="Update ROOMS set STATUS='HALF OCCUPIED' where ROOM_NO='{}'".format(rroomno,)
                                        mycursor.execute(query)
                                        mycon.commit()
                                    else:
                                        query="Update ROOMS set STATUS='VACANT' where ROOM_NO='{}'".format(rroomno,)
                                        mycursor.execute(query)
                                        mycon.commit()
                                    print("#ROOM STATUS UPDATED#")
                                mycursor.execute(stat)
                                mycon.commit()
                                print("#DATA OF RESIDENT DELETED#")
                    elif delete=="no":
                        print("OPERATION CANCELLED")
                    else:
                        print("INVALID INPUT")
            else:
                print("INVALID INPUT")
                print("Contact no. must be a 10 digit number.")
            ans=input("Want to delete data of more residents?(yes/no):")

def dues(mycursor, mycon):                                  #rent defaulters
    pdate=date.today()
    pdate=str(pdate)
    if int(pdate[5:7])==1:                                          #if block to subtract 1 month from due date
        prdate=str(int(pdate[0:4])-1)+pdate[4]+str(12)+pdate[7:]
    elif int(pdate[5:7]) in (5, 7, 10, 12) and int(pdate[8:])==31:
        prdate=pdate[0:5]+str(int(pdate[5:7])-1)+pdate[7]+str(30)
    elif int(pdate[5:7])==3 and int(pdate[8:]) in (29, 30, 31): 
        if int(pdate[0:4])%4==0 and int(pdate[8:])==29: 
            prdate=pdate[0:5]+str(int(pdate[5:7])-1)+pdate[7:]
        elif int(pdate[0:4])%4==0 and int(pdate[8:]) in (30, 31):
            prdate=pdate[0:5]+str(int(pdate[5:7])-1)+pdate[7]+str(29)
        else:
            prdate=pdate[0:5]+str(int(pdate[5:7])-1)+pdate[7]+str(28)
    else:
        prdate=pdate[0:5]+str(int(pdate[5:7])-1)+pdate[7:]
    statement="Select* from RESIDENTS where ONE_MONTH_BEFORE_DUE_DATE<='{}' order by ONE_MONTH_BEFORE_DUE_DATE asc".format(prdate,)
    mycursor.execute(statement)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("All dues are clear")
    else:
        print("RENT PAYMENT POLICY: 1.Security deposit is 1 month rent \n                     2.Rent must be paid monthly\n")
        print("Total no. of residents with pending dues are=", count)
        print("Details of all residents with pending dues are as follows:")
        print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
        for row in data:
            row=list(row)
            row[7]=str(row[7])
            row[2]=str(row[2])
            row=tuple(row)
            print(row)
            if int(row[7][5:7])==12:                                #if block to find due date
                dd=str(int(row[7][0:4])+1)+row[7][4]+"01"+row[7][7:]
            elif int(row[7][5:7]) in (3, 5, 8, 10) and int(row[7][8:])==31:
                dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(30)
            elif int(row[7][5:7])==1 and int(row[7][8:]) in (29, 30, 31):
                if int(row[7][0:4])%4==0 and int(pdate[8:])==29:
                    dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7:]
                elif int(pdate[0:4])%4==0 and int(pdate[8:]) in (30, 31):
                    dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(29)
                else:
                    dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(28)
            else:
                dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7:]
            print("=>", row[0], " cleared all the dues only till ", dd, ".", end="")
            print(" Therefore, according to the RENT PAYMENT POLICY, rent that is due, is from ", dd, ".")
        answ=input("Want to clear any dues?(yes/no):")
        if answ=="yes":
            clear_dues(mycursor, mycon)            
        elif answ=="no":
            nothing="nothing"
        else:
            print("INVALID INPUT")
        
def clear_dues(mycursor, mycon):                            #clear dues
    mycursor.execute("Select* from RESIDENTS")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("Currently no residents")
    else:
        print("Please enter the following details of the resident to clear his dues:")
        rname=input("Name:")
        rname=rname.upper()
        rcontactno=input("Contact No.:")
        rcontactno=rcontactno.strip()
        if len(rcontactno)==10 and rcontactno.isdigit():                         #contact no. is a 10 digit number
            rroomno=input("Room no.: ")
            rroomno=rroomno.upper()
            querys="Select* from RESIDENTS where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(rname, rcontactno, rroomno)
            mycursor.execute(querys)
            data=mycursor.fetchall()
            count=mycursor.rowcount
            if count==0:
                print("INVALID INPUT")
                print("The Resident doesn't exist.")
            else:                           #if resident exists
                print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
                for row in data:
                    row=list(row)
                    row[7]=str(row[7])
                    row[2]=str(row[2])
                    row=tuple(row)
                    print(row)
                    if int(row[7][5:7])==12:                        #if block to find due date
                        dd=str(int(row[7][0:4])+1)+row[7][4]+"01"+row[7][7:]
                    elif int(row[7][5:7]) in (3, 5, 8, 10) and int(row[7][8:])==31:
                        dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(30)
                    elif int(row[7][5:7])==1 and int(row[7][8:]) in (29, 30, 31):
                        if int(row[7][0:4])%4==0 and int(pdate[8:])==29:
                            dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7:]
                        elif int(pdate[0:4])%4==0 and int(pdate[8:]) in (30, 31):
                            dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(29)
                        else:
                            dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7]+str(28)
                    else:
                        dd=row[7][0:5]+str(int(row[7][5:7])+1)+row[7][7:]
                    print("=>", row[0], " cleared all the dues till ", dd, ".")
                print("Above information might be helpful in proceeding...")
                dates=input("Please enter a new date upto which all the dues are cleared(YYYY-MM-DD):")
                if int(dates[5:7])==1:                              #if block to subtract 1 month from new due date
                    dates=str(int(dates[0:4])-1)+dates[4]+str(12)+dates[7:]
                elif int(dates[5:7]) in (5, 7, 10, 12) and int(dates[8:])==31:
                    dates=dates[0:5]+str(int(dates[5:7])-1)+dates[7]+str(30)
                elif int(dates[5:7])==3 and int(dates[8:]) in (29, 30, 31):
                    if int(dates[0:4])%4==0 and int(dates[8:])==29:
                        dates=dates[0:5]+str(int(dates[5:7])-1)+dates[7:]
                    elif int(pdate[0:4])%4==0 and int(pdate[8:]) in (30, 31):
                        dates=dates[0:5]+str(int(dates[5:7])-1)+dates[7]+str(29)
                    else:
                        dates=dates[0:5]+str(int(dates[5:7])-1)+dates[7]+str(28)
                else:
                    dates=dates[0:5]+str(int(dates[5:7])-1)+dates[7:]
                queryss="Update RESIDENTS set ONE_MONTH_BEFORE_DUE_DATE='{}' where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(dates, rname, rcontactno, rroomno)
                mycursor.execute(queryss)
                mycon.commit()
                print("#DUES CLEARED#")
        else:
            print("INVALID INPUT")
            print("Contact no. must be a 10 digit number.")

def food_residents(mycursor):                               #residents availing food facility
    mycursor.execute("Select* from RESIDENTS where FOOD_REQ='YES'")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Food facility is not being availed by anyone")
    else:
        print("Total no. of residents availing food facility are=", count)
        print("Details of residents availing food facility are as follows:")
        print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
        for row in data:
            row=list(row)
            row[7]=str(row[7])
            row[2]=str(row[2])
            row=tuple(row)
            print(row)

def ch_food(mycursor, mycon):                               #change food req.
    mycursor.execute("Select* from RESIDENTS")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("Currently no residents")
    else:
        print("Please enter the following details of the resident to change food requirement:")
        rname=input("Name:")
        rname=rname.upper()
        rcontactno=input("Contact No.:")
        rcontactno=rcontactno.strip()
        if len(rcontactno)==10 and rcontactno.isdigit():     #contact no. is a 10 digit number
            rroomno=input("Room no.: ")
            rroomno=rroomno.upper()
            querys="Select* from RESIDENTS where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(rname, rcontactno, rroomno)
            mycursor.execute(querys)
            data=mycursor.fetchall()
            count=mycursor.rowcount
            if count==0:
                print("INVALID INPUT")
                print("The Resident doesn't exist.")
            else:                           #if resident exists
                print("\n\
('NAME', 'CONTACT NO.', 'DOB', 'ADDRESS', 'ROOM NO.', 'ROOM TYPE', 'FOOD REQ.', 'ONE_MONTH_BEFORE_DUE_DATE')\n")
                for row in data:
                    row=list(row)
                    row[7]=str(row[7])
                    row[2]=str(row[2])
                    row=tuple(row)
                    print(row)
                    if row[6]=="YES":
                        print("=>", row[0], " is availing food facility.")
                    else:
                        print(row[0], " is not availing food facility.")
                print("Above information might be helpful in proceeding...")
                foodreq=input("Please enter your choice, Food requirement(yes/no):")
                foodreq=foodreq.upper()
                queryss="Update RESIDENTS set FOOD_REQ='{}' where NAME='{}' and CONTACT_NO='{}' and ROOM_NO='{}'".format(foodreq, rname, rcontactno, rroomno)
                mycursor.execute(queryss)
                mycon.commit()
                print("#FOOD REQUIREMENT UPDATED#")
        else:
            print("INVALID INPUT")
            print("Contact no. must be a 10 digit number.")










