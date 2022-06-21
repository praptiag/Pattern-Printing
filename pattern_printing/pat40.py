"""
        1 
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range((2*row)-1,0,-1):
        print(syb,end=" ")
    print("\n")