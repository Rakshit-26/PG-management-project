def pgmap():                                    #Displays floor map
    print("Ground Floor=>")                     #ground floor map
    print("\
    \t\t\t+--------+------------+--------+\n\
    \t\t\t|        |            |        |\n\
    \t\t\t|        |  STAIRCASE |        |\n\
    \t\t\t|   G02  +------------+  G01   |\n\
    \t\t\t|        |            |        |\n\
    \t\t\t+--------+            +--------+\n\
    \t\t\t|                              |\n\
    \t\t\t E          +------+           |\n\
    \t\t\t|           |   R  |           |\n\
    \t\t\t+-----------+------+-----------+")
#
#
    print("Other Floors=>")                     #other floors' map
    print("\
    \t\t\t+--------+-----------+--------+\n\
    \t\t\t|        |           |        |\n\
    \t\t\t|        | STAIRCASE |        |\n\
    \t\t\t|   F02  +-----------+  F01   |\n\
    \t\t\t|        |           |        |\n\
    \t\t\t+--------+           +--------+\n\
    \t\t\t|        |           |        |\n\
    \t\t\t|        +-----+-----+        |\n\
    \t\t\t|   F04(2P)    |     F03(2P)  |\n\
    \t\t\t|              |              |\n\
    \t\t\t+--------------+--------------+\n")
    print("where,R denotes RECEPTION\n\
      E denotes ENTRY\n\
  and F denotes Floor number(where, F=1/2/3)")
