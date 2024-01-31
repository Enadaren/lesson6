import os
a=int(input("Input under-root value: "))
n=int(input("root-value: "))
x0=a/n +1
x1=a/n
i=0
while abs(x0-x1)>=0.0001:
    x0=x1
    x1=((n-1)*x0+a/(x0**(n-1)))/n
    i=i+1
print("root", n, "of", a, ":", '%.4f' % x1,"\n",i,"steps")


