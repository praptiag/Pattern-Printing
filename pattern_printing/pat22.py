"""
E E E E E 
D D D D
C C C
B B
A
"""
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(64+i),end=" ")
    print("\n")