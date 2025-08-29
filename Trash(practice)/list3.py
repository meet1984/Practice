data=[]
choice=0
while choice==1:
        rollno=int (input ("Enter rollno: "))
        name=input ("Enter name : ")
        eng=int (input ("Enter english marks: "))
        maths=int (input ("Enter maths marks : "))
        sci=int (input ("Enter science marks: ")) 
        sst=int (input ("Enter sst marks: "))
        total=eng+maths+sci+sst
        if total>250: 
            grade="A"
        elif total>220:
            grade="B"
        elif total>180: 
            grade="C"
        else:
            grade="D"
        rec=[rollno, name, eng, maths, sci, sst, total, grade] 
        data. append (rec)
        choice=int (input ("Press 1 to continue : "))


for i in data:
    print ("*"*30)
    print ("Rollno    : ",i[0])
    print ("Name     :",i[1])
    print ("Eng         : ", i [2])
    print ("Maths    :", i [3])
    print ("Sci          : ", i[4])
    print ("Sst         : ", i [5])
    print ("Total       :", i[6])
    print ("grade       : ", i [7])
    print ("*"*30)

while choice!=8:
    input()
    print ("\n\t\tMain Menu")
    print ("\n\t\t\tl. Add Record")
    print ("\n\t\t\t2. Search Record") 
    print ("\n\t\t\t3. All Record") 
    print ("\n\t\t\t4. Topper")
    print ("\n\t\t\t5. Gradewise Details")
    print ("\n\t\t\t6. Modify Records")
    print ("\n\tt\t7. Delete Record")
    print ("\n\t\t\t8. Exit")
    choice=int (input ("\n\t\t\tEnter your choice : ")) 
    if choice==1:
        rollno=int (input ("Enter rollno : "))
        name=input ("Enter name : ")
        eng=int (input ("Enter english marks : ")) 
        maths=int (input ("Enter maths marks:") )
        sci=int (input ("Enter science marks:") )
        sst=int (input ("Enter sst marks : "))
        total=eng+maths+sci+sst
        if total>250: 
            grade="A"
        elif total>220:
            grade="B"
        elif total>180: 
            grade="C"
        else:
            grade="D"
        rec=[rollno, name, eng, maths, sci, sst, total, grade]
        data. append (rec)
    elif choice==4:
        hi=0
        cn=0
        for i in data:
            if hi<i[6]:
                hi=i[6]
                pos=cn
            cn+=1 
        print ("*"*30)
        print ("Rollno : ",data[pos][0])
        print ("Name : ",data[pos][1])
        print ("Eng     : ",data[pos][2])
        print ("Maths : ",data[pos][3])
        print ("Sci       : ",data[pos][4])
        print ("Sst       : ",data[pos][5])
        print ("Total   : ",data[pos][6])
        print ("Grade : ",data[pos][7])
        print ("*"*30)            
    elif choice==6:
        rn=int(input("Enter Rollno:"))
        for i in data:
            if rn==i[0]:
                print ("\n\t\tModify Menu")
                print ("\n\t\t1.Name")
                print ("\n\t\t2.Eng")
                print ("\n\t\t3.Maths")
                print ("\n\t\t4.Sci")
                print ("\n\t\t5.Sst")
                choice=int(input("Enter choice :."))
                if choice==1:
                    i[1]=input("Enter new Name : ")
                elif choice==2:
                    i[2]=int(input("Enter Eng marks : "))
                i[6]=i[2]+i[3]+i[4]+i[5]
                break
    elif choice==2:
        rn=int(input("Enter Rollno:"))
        for i in data:
            if rn==i[0]:
                  print ("*"*30)
                  print ("Rollno    : ",i[0])
                  print ("Name     :",i[1])
                  print ("Eng         : ", i [2])
                  print ("Maths    :", i [3])
                  print ("Sci           : ", i[4])
                  print ("Sst           : ", i [5])
                  print ("Total        :", i[6])
                  print ("grade       : ", i [7])
                  print ("*"*30)
                  break
    elif choice==5:
        grade=input("Enter Grade :")
        for i in data:
            if i[7]==grade.upper():
                  print ("*"*30)
                  print ("Rollno   : ",i[0])
                  print ("Name     :",i[1])
                  print ("Eng      : ", i [2])
                  print ("Maths  :", i [3])
                  print ("Sci        : ", i[4])
                  print ("Sst       : ", i [5])
                  print ("Total    :", i[6])
                  print ("grade  : ", i [7])
                  print ("*"*30)
                  
    elif choice==3:
        for i in data:
            print ("*"*30)
            print ("Rollno   : ",i[0])
            print ("Name     :",i[1])
            print ("Eng      : ", i [2])
            print ("Maths  :", i [3])
            print ("Sci        : ", i[4])
            print ("Sst       : ", i [5])
            print ("Total    :", i[6])
            print ("grade  : ", i [7])
            print ("*"*30)
            
    elif choice==7:
        rn=int(input("Enter roll no:"))
        for i in data :
             if rn==i[0] :
                 data.remove(i)
                 break
remove function 
