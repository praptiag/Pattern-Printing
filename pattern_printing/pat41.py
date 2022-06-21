"""
        A 
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range(1,((2*row)-1)+1):
        print(chr(64+syb),end=" ")
    print("\n")