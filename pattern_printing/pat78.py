"""
        1   
      1   2   
    1   2   3
  1   2   3   4
1   2   3   4   5
  1   2   3   4
    1   2   3
      1   2
        1
"""
size=4
for i in range(size,-(size+1),-1):
    for j in range(1,abs(i)+1):
        print(" ",end=" ")
    p=1
    for k in range(size,abs(i)-1,-1):
        print(p,end="   ")
        p+=1
    print('\n')