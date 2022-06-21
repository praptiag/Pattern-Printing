"""
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2
        1
"""
row=5
for i in range(row,0,-1):
    for space in range (i,row+1):
        print(" ",end=" ")
    for syb in range((2*i)-1,0,-1):
        print(i,end=" ")
    print("\n")