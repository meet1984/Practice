# Typle is a read only version of list 
# Tuple is a colletcion of , seperated values which are inclosed in small bracket (which is optional)
# Tuple is immutable it means we cannot make changes in tuple object
# when we have the pre set of values then we should use the tuple 
# Tuple is fixed in values 
# It follow the insertion order
# tuple follow the indexing and slicing
# It does not follow item assignment

# find largest no without using max


x=[10,200,100,30,40,5]
y=x[0]
z=x[0]
# MAX
for i in x :
    if i>y :
       y = i 
# MIN
    if i<z:
        z=i
print("Max :",y)
print("Min :",z)       