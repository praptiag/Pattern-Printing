"""
D 
C D
B C D
A B C D
B C D
C D
D
"""
num=3
for i in range(num,-(num+1),-1):
    for j in range(abs(i),num+1):
        print(chr(65+j),end=" ")
    print('\n')