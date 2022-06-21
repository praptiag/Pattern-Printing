"""
        0 
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(totalRows-1,row-1,-1):
        print(" ",end=" ")
    for syb in range ((2*row)-1,0,-1):
        print(abs(syb-row),end=" ")
    print('\n')