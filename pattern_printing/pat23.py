"""
E D C B A 
E D C B
E D C
E D
E
"""
for i in range(0,5):
    for j in range(5,i,-1):
        print(chr(64+j),end=" ")
    print("\n")