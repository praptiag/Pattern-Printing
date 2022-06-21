from html.entities import name2codepoint

#Fibonacci pyramid

"""
0 
0 1
0 1 1
0 1 1 2
0 1 1 2 3
"""
n=5
n1=0
n2=1
r=0
for i in range(0,n):
    for j in range(0,i+1):
        print(r,end=" ")
        n1=n2
        n2=r
        r=n1+n2
    n1=0
    n2=1
    r=0
    print('\n')