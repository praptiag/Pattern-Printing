"""
        A 
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""
row=5
for i in range(1,row+1):
    for space in range(i,row):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(i-1,0,-1):
        print(chr(64+k),end=" ")
    print("\n")