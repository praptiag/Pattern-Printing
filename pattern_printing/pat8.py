"""
E E E E E 
D D D D D
C C C C C
B B B B B
A A A A A
"""
for i in range(5,0,-1):
    for j in range (0,5):
        print(chr(64+i),end=' ')
    print('\n')