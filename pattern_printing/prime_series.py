#prime no
""" 2 3 5 7 11 13 17  """
n=17
count=0
num=1
while(num<=n):
    for i in range(1,num):
        if num%i==0:
            count+=1
    if count==1:
        print(num,end=" ")
    count=0
    num+=1

