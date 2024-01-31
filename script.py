import os
a=int(input("Input under-root value: "))
n=int(input("root-value: "))
x0=a/2+1
x1=a/2
while abs(x0-x1)>=0.0001:
    x0=x1
    x1=((n-1)*x0+a/(x0**(n-1)))/n
print("root", n, "of", a, ":", '%.4f' % x1)


