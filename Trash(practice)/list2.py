# data=[10,20,30]
# data.append(40)
# data.append([50,60,70])
# data.extend([111,3222,444])
# data.insert(4,800)
# print(data)



# data=[]
# while True :
 # name=input("enter name :")
 # rollno=int(input("enter roll no :"))
 # if name=="" and rollno==0:
   # break
 
 # data.append([name,rollno])
# print(data)

# ADD RECORD SEARCH RECORD ON RECORD TOPPER STUDENT GRADE WISE DETAIL MODIFY DETAIL DELETE RECORD EXIT


data=[]
while choice!=8 :
    print("\n\n\tMAin menu")
    print("\n\n\t1 Add Record")
    print("\n\n\3 search record")
    print("\n\n\t4 All record")
    print("\n\n\t5 topper")
    print("\n\n\t6 Gradewise Detail")
    print("\n\n\t7 modify Record")
    print("\n\n\t8 Delete Record")
    print("\n\n\t9 Exit")
    choice=int(input("Enter your Choice:"))
    if choice==1 :
        rollno=input("enter roll no:")
        name=input("enter name:")
        eng=int(input("enter english marks :"))
        hin=int(input("enter hindi marks:"))
        mat=int(input("enter math marks :"))
        totalmarks=eng+hin+mat
        if totalmarks>=280 :
          print("grade A")
        elif totalmarks>=240 :
          print("grad B")
        elif totalmarks>=200 :
          print("grade C")
        else  :
         print("grade D")
         rec=[rollno,name,m2,m2,m3,total,Grade]
         data.append(rec)
    elif choice==2 :
        rn=int(input(enter roll no:))
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
    elif choice==3 :
        for i in data :
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
    elif choice==4 :
        hi=0
        cn=0
        for i in data:
         if hi<=i[6]
            hi=i[6] 
            ps=cn
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
    elif choice==5 :
                