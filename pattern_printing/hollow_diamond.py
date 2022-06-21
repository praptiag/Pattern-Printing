"""
* * * * *  * * * * *
* * * *      * * * *
* * *          * * *
* *              * *
*                  *
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *
"""

n=5
#upper half of the pattern
for i in range(0,n):
    for j in range(0,2*n):
        #upper left triangle
        if (i+j<=n-1):
            print("*",end="")
        else:
            print(" ",end="")
        #upper right triangle
        if(i+n)<=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#lower half of the pattern
for i in range(0,n):
    for j in range(0,2*n):
        #bottom left traingle
        if i>=j:
            print("*",end="")
        else:
            print(" ",end="")

        #bottom right triangle
        if i>= (2*n-1)-j:
            print("*",end="")
        else:
            print(" ",end="")
    print()


