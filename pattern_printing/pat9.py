"""
E D C B A 
E D C B A
E D C B A
E D C B A
E D C B A
"""
for i in range(0,5):
    for j in range (5,0,-1):
        print(chr(64+j),end=' ')
    print('\n')