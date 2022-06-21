"""
        A 
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range(0,(2*row)-1):
        print(chr(64+row),end=" ")
    print("\n")