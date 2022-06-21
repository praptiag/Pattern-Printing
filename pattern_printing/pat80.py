"""
        A   
      A   B
    A   B   C   
  A   B   C   D
A   B   C   D   E
  B   C   D   E
    C   D   E
      D   E
        E

"""
size=4
for i in range(size,-(size+1),-1):
    for j in range(1,abs(i)+1):
        print(" ",end=" ")
    if i>=0:
        p=1
    else:
        p=j+1
    for k in range(size,abs(i)-1,-1):
        print(chr(64+p),end="   ")
        p+=1
    print('\n')