# write a program to enter a string and the frquency of each element of string

# s1=input("enter a value")
# s2=""

# for i in s1 :
    # if i not in s2 :
        # print("frequency of",i,"is",s1.count(i))
        # s2=s2+i
        
        
        
# write a program to validate a email

# email=input("enter your mail :")
# z=email[0].isalpha()
# x=email.find("@")!=-1 
# y=email.endswith(".com") or email.endswith(".in") 
          
# if x and y and z:         
          # print("validate")
# else  :
    # print("not valid")
    # if not email[0].isalpha() :
        # print("email must start with alphabet")
    # if email.find("@")==-1 :
        # print("please enter @ symbol")
    # if not (email.endswith(".com") or email.endswith(".in")):
        # print("email adderess must end with .com or .in")
        
        
# count thr no of words that start with the vovel in given sentence 



# x="hello how are you is uu yy"
# x=x.split()
# w=0
# for i in x:
    # if i[0] in ['a','i','e','o','u']:
        # w+=1
         
# print(w)


# a='a'
# s="how are you a a"
# for i in s:
    # if i==a:
        # print("pos of",a,"is",s.find(a))
# print(x)
      
  
a="aaabbbcccddd"  
print(a.count("a",5,len(a)))

s="aaabbbcccaaabbbccc"
print(s.find("c"))


x="aaabbbcccddd"
pos=0
while True :
      pos=x.find("a",pos,len(x))
      if pos==-1:
       break
      print(pos)
      pos+=1
      
      
z="hello"
m="Luck"
n="You"
l="{},{},{} welocome guys"
print(l.format(z,m,n))

print(f"{z},{m},{n} are guys")



q="you are gay person"
q=q.replace("gay","good")
print(q)

a="python is difficult HTML is difficult and binary is difficult"
a=a.replace("difficult","easy",2)
print(a)


s1="aabb xyz Hello"
# ans=bbaa zyx olleH

s1=s1.split()
print(s1)
for i in s1 :
 print(s[i].reverse())
 i+=1