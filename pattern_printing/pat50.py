"""
  1 2 3 4 5 6 7 
    1 2 3 4 5
      1 2 3
        1
"""
row=4
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for syb in range (1,((2*i)-1)+1):
        print(syb,end=" ")
    print("\n")
