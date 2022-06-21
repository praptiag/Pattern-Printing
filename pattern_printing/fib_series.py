#fibonacci series
""" 1 1 2 3 5 8 13 21  """
n=22
a,b=0,1
c=a+b
while(c<n):
    print(c,end=" ")
    c=a+b
    a=b
    b=c
    