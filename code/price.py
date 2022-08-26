def r_price1p():                            #Displays price of 1P type rooms
    myfile=open("prices.txt", "r")
    line1=myfile.readline()
    return(line1.strip())
    myfile.close()

def r_price2p():                            #Displays price of 2P type rooms
    myfile=open("prices.txt", "r")
    line1=myfile.readline()
    line2=myfile.readline()
    return(line2.rstrip())
    myfile.close()

def ch_rent():                              #Changes rent of rooms
    file=open("prices.txt", "r")
    data=file.readlines()
    file.close()
    s1="Rs."
    s2=" p.m.\nRs."
    s3=" p.m.\n\n\
NOTE:Line1 denotes: Price of 1P Rooms\n          \
Line2 denotes: Price of 2P Rooms"
    print("Please specify the rent you want to update:")
    print("Press[1 for 1P rooms], [2 for 2P rooms]")
    option=int(input("Enter your choice(1/2)=>"))
    if option==1:
        rent=input("Please enter the new rent:")
        rent=rent.strip()
        if rent.isdigit():
            myfile=open("prices.txt", "w")
            data[0]=s1+rent+s2[0:7]
            myfile.writelines(data)
            myfile.close()
            print("#RENT UPDATED#")
        else:
            print("INVALID INPUT")
            print("Enter only numeric value(for rent)")
    elif option==2:
        rent=input("Please enter the new rent:")
        rent=rent.strip()
        if rent.isdigit():
            myfile=open("prices.txt", "w")
            data[1]=s1+rent+s3[0:7]
            myfile.writelines(data)
            myfile.close()
            print("#RENT UPDATED#")
        else:
            print("INVALID INPUT")
            print("Enter only numeric value(for rent)")
    else:
        print("INVALID INPUT")


'''
Rs.13000 p.m.
Rs.9000 p.m.

NOTE:Line1 denotes: Price of 1P Rooms
          Line2 denotes: Price of 2P Rooms'''
