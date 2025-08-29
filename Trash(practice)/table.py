# program to create a table
i=int(input("enter a no:"))
s=int(input("enter starting no:"))
e=int(input("enter ending no :"))

if s>=e :
    # c=s
    # s=e
    # e=c or
    (s, e)=(e, s)
    
while s<=e :
    print(i,"*",s,"=",i*s)
    s+=1
# else :
  # while e<=s :
      # print(i,"*",e,"=",i*e)
      # e+=1
