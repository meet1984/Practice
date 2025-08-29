print("Topic: Exception Handling")

try :
    a=int(input("Enter no A"))
    b=int(input("Enter no B"))
    c=a/b
    print("Result = ",c)
    print("try executed")
except :
    print("error handeld")
else :
    print("i was executed beacuse no error ouccered")
finally :
    print("it has to be executed because it is in finally block")
