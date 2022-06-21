#fibonacci series
"""
1 
1 2
3 5 8
13 21 34 55
89 144 233 377 610
"""
n1=0
n2=1
r=n1+n2
for i in range(0,5):
    for j in range(0,i+1):
        print(r,end=" ")
        r=n1+n2
        n1=n2
        n2=r
    print('\n')