"""
        1   
      2   2
    3   3   3
  4   4   4   4
5   5   5   5   5
  4   4   4   4
    3   3   3
      2   2
        1
"""
p=1
size=4
for i in range(size,-(size+1),-1):
    for j in range(0,abs(i)):
        print(" ",end=" ")
    for k in range(size,abs(i)-1,-1):
        print(p,end="   ")
    if i>0:
            p+=1
            
    else:
            p-=1
    print('\n')