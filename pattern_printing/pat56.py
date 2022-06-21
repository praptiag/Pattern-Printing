"""
3 
2 3
1 2 3
0 1 2 3
1 2 3
2 3
3
"""
row=3
for i in range(row,-(row+1),-1):
    for j in range(abs(i),row+1):
        print(j,end=" ")
    print('\n')