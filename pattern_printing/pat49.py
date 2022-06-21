"""
  7 7 7 7 7 7 7 
    5 5 5 5 5
      3 3 3
        1
"""
row=4
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for syb in range((2*i)-1,0,-1):
        print((2*i)-1,end=" ")
    print("\n")