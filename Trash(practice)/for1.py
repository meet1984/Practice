# x=int(input("enter the value"))
# y=int(input("enter ending value"))

# for i in range(x,y):
 # print(i)
 
 

# for i in range(0,10):
  # for j in range(0,i+1):
    # print("*",end="")
  # print()
  
# for i in range(10,0,-1):
  # for j in range(0,i-1):
    # print("*",end="")
  # print()
  
x=int(input("Enter staring value"))
y=int(input("Enter ending value"))
for i in range(x,y,):
  for j in range(0,i-1):
    print("*",end="")
  print()