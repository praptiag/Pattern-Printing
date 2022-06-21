"""
A B C D E 
A B C D 
A B C   
A B
A
"""
for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(65+j),end=" ")
    print('\n')