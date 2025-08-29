# A-Z (65-90)
# a-z (97-122)
# 0-9 (48-57)

a=ord(input("enter a value:"))
if a>=65 and a<=90 :
    print("it is uppercase")
elif a>=97 and a<=122 :
    print("it is lowercase")
elif a>=48 and a<=57 :
    print("it is digit")
else :
    print("special charcter")    