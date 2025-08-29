# write a program to eneter string
    # upper
    # lower
 
# x="aaaaBBB123###"
# u=0
# l=0
# sp=0
# d=0
# for i in x :
 # if i.isupper() :
        # u+=1
 # elif i.islower():
    # l+=1
 # elif i.isdigit():
    # d+=1
 # else :
    # sp+=1
# print("upper:",u)
# print("lower:",l)
# print("digit:",d)
# print("specialchar:",sp)




# program to no of words

# # x="hello who are you"
# # w=1

# # # for i in x:
    # # # if i.isspace():
        # # # w+=1
 # print("no of words:",w)

# x="hey  budy  !!   who are you"
# w=1

# for i in range(len(x)):
 # if x[i]==" " and x[i+1]!=" " :
     # w+=1
# print(w)

# write a program to print a3b3c5

# a="a3b3c5"
# s=""
# for i in a:
    # if i.isalpha():
     # c=i
    # else :
       # s=s+c*int(i) 
    # print(s)
    
# s=a3b3c5
 # adbech
 
# s="a3b3c5"
# a=""
# for i in s:
     # if i.isalpha():
      # c=i
     # else :
      # w=ord(c)
      # z=w+int(i)
      # w=chr(z)
      # a=a+c+w
# print(a)

# def myInt(a):    # a="123"
    # s=0
    # # convert int
    # for i in a:
        # c=ord(i)-48
        # s=s*10+c
    # return s
# s=myInt("1853")
    
# print(type(s))




# convert in uppercase
# 65-90

a="abcD"
s=""
for i in a:
   if ord(i)>=97 and ord(i)<=122 :
     c=chr(ord(i)-32) 
     s=s+c
   else :
     d=i
     s=s+d  
print(s)




