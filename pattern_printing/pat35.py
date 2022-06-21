"""
        1 
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range(0,(2*row)-1):
        print(row,end=" ")
    print("\n")