"""
1 
1 2 
1   3
1     4
1 2 3 4 5
"""
row=5
for i in range(1,row+1):
    for j in range(1,i+1):
        if j==1 or j==i or i==row:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()