a=int(input("enter 1st number"))
b=int(input("enter 2st number"))
c=int(input("enter 3st number"))
d=int(input("enter 4st number"))
e=int(input("enter 5st number"))
if a>b and a>c and a>d and a>e:
    print("a is largest")
elif b>c and b>d and b>e:
    print("b is largest")
elif c>d and c>e :
    print("c is largeat")
elif d>e :
    print("d is greater")
else:
    print("e is greater")
