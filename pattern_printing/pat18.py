"""
A A A A A 
B B B B
C C C
D D
E
"""
for i in range(0,5):
    for j in range(5,i,-1):
        print(chr(65+i),end=" ")
    print('\n')