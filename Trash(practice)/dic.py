
data={"lana":"1 jan","denial":"1 feb","mia":"1 mar","deni":"1 apr"}
while True :
    name=input("Enter your name:") 
    if name == "" :
       break
    if name in data :
       print(name, "DOB is ",data[name])   
    else :
       print("name not found")         
       choice=int(input("enter 1 to add name and 2 to not and press any other key to  to see updated Data"))
       if choice == 1 :
           name=input("enter name you want to add :")
           dob=input("enter DOB you want to add:")
           data[name]=dob
       elif choice ==2 :
            break
       else :
           print(data)