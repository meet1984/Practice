# write a program to reverse a no?
# write a program to check no. is pelendrom or not?
# write a program to find sum of digit of a no.?
# write a program to check no. is armstrong or not
# write a program to print all armstrong no from 1 to 1000?
# write a program to print all pelendrom no. from 1 to 1000?

# Q1
 
# num=int(input("enter  a value"));
# a=num ;
# rev=0

# # b=num%10;
# # rev=rev*10+b;
# # num=num//10;

# # c=num%10;
# # rev=rev*10+c;
# # num=num//10;
 
# # print(rev)
# while num!=0 :
    # b=num%10
    # rev=rev*10+b
    # num=num//10
    
# print(rev)
 
# if a==rev :
 # print("it is pallendrome")
# else :
 # print("it is not pallendrome")
 
 
no=int(input("enter a no:"));
ori=no
d=0
l=len(str(no))
while no!=0 :
    b=no%10;
    no=no//10
    d=d+(b**l)
if d==ori :
     print("it is armstrong")
else :
     print("not")     
 
 
