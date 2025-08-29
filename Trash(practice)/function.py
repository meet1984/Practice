# def star() :
   # print("hello Buddy")
# def line() :
    # for i in range(1,10):
     # print("*-",end="")
# star()
# line()

# star()

def line(x) :
    for i in range(1,10):
      print(x,end="")
    print()
line("!")
line("#")
line("@")
line("_")


def  sum(a,b) :
    # print("sum of a and b =",a+b)
    # print()
    return a+b 
x=sum(5,5)
y=sum(10,10)
z=sum(x,y)
print("Total sum :",z)

print(sum(sum(5,5),sum(5,5)))



def iseven(a):
    if a%2==0 :
        return True 
    return False 

print("10 is even :",iseven(10))