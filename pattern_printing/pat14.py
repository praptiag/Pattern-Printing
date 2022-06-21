"""
A 
A B
A B C
A B C D
A B C D E
"""
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+j),end=" ")
    print("\n")