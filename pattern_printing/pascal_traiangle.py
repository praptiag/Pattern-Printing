"""
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""
n=5
#O(N)
for i in range(n):
    print(' '*(n-i),end="")
    print(' '.join(map(str,str(11**i))))

#O(n^2)
from math import factorial
from msvcrt import kbhit 
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")

    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
    print()

#O(n^2)
for i in range(1,n+1):
    # for j in range(0,n-i+1):
    #     print(' ',end="")
    c=1
    for j in range(1,i+1):
        print(' ',c,sep='',end='')
        #using binomial coefficient
        c=c*(i-j)//j
    print()