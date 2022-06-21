"""
        A   
      B   B
    C   C   C
  D   D   D   D
E   E   E   E   E
  D   D   D   D
    C   C   C
      B   B
        A
"""
size=4
p=0
for i in range(size,-(size+1),-1):
    for j in range(1,abs(i)+1):
        print(" ",end=" ")
    for k in range(size,abs(i)-1,-1):
        print(chr(65+p),end="   ")
    if(i>0):
            p+=1
    else:
            p-=1
    print('\n')