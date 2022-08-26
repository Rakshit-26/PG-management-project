def t_rooms(mycursor):                              #all rooms' details
    mycursor.execute("Select* from ROOMS")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    print("Total no. of rooms are=", count)
    print("Details of rooms are as follows:")
    print("\n\
('ROOM NO.', 'ROOM TYPE', 'FLOOR', 'STATUS')\n")
    for row in data:
        print(row)
        
def unocc_rooms(mycursor):                          #all unocc. rooms
    mycursor.execute("Select* from ROOMS where STATUS<>'OCCUPIED'")
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
            
def unocc_1prooms(mycursor):                        #all unocc. 1P rooms
    mycursor.execute("Select* from ROOMS where STATUS<>'OCCUPIED' and R_TYPE='1P'")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("All 1P rooms are occupied")
    else:
        print("Total no. of 1P unoccupied rooms are=", count)
        print("Details of 1P unoccupied rooms are as follows:")
        print("\n\
('ROOM NO.', 'ROOM TYPE', 'FLOOR', 'STATUS')\n")
        for row in data:
            print(row)

def unocc_2prooms(mycursor):                        #all unocc. 2P rooms
    mycursor.execute("Select* from ROOMS where STATUS<>'OCCUPIED' and R_TYPE='2P'")
    data=mycursor.fetchall()
    count=mycursor.rowcount
    if count==0:
        print("Sorry!!")
        print("All 2P rooms are occupied")
    else:
        print("Total no. of 2P unoccupied rooms are=", count)
        print("Details of 2P unoccupied rooms are as follows:")
        print("\n\
('ROOM NO.', 'ROOM TYPE', 'FLOOR', 'STATUS')\n")
        for row in data:
            print(row)

def F0_rooms(mycursor, y):                          #unocc. rooms(floorwise)
    st="Select* from ROOMS where STATUS<>'OCCUPIED' and FLOOR='{}'".format(y,)
    mycursor.execute(st)
    data=mycursor.fetchall()
    count=mycursor.rowcount
    z=y.lower()
    if count==0:
        print("Sorry!!")
        print("All rooms on ", z, " floor are occupied")
    else:
        print("Total no. of unoccupied rooms on ", z, " floor are=", count)
        print("Details of unoccupied rooms on ", z, " floor are as follows:")
        print("\n\
('ROOM NO.', 'ROOM TYPE', 'FLOOR', 'STATUS')\n")
        for row in data:
            print(row)

