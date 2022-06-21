"""
3 
3 2
3 2 1
3 2 1 0
3 2 1
3 2
3
"""
# col=4
# for i in range(col-1,-1,-1):
#     for j in range(col-1,i-1,-1):
#         print(j,end=" ")
#     print("\n")
# for i in range(1,col):
#     for j in range(1,(col-i)+1):
#         print(col-j,end=" ")
#     print("\n")

row=3
for i in range(row,-(row+1),-1):
    for j in range(row,abs(i)-1,-1):
        print(j,end=" ")
    print('\n')