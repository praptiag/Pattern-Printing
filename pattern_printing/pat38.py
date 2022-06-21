
"""
        A 
      C C C
    E E E E E
  G G G G G G G
I I I I I I I I I
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range(0,(2*row)-1):
        print(chr(64+((2*row)-1)),end=" ")
    print("\n")