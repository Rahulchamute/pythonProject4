##dict
#dict1={"key1":1,"key2":2,"key3":3}
#print(dict1)

# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name)

# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020,"Name":"Ankit"}
# print(student_name)

# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name["Name"])
#
# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name["Roll_no"])

# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name.get("Name"))
#
# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name.get("name"))

# Employee_Details={
#     "Employee_Name"   :"Prashant",
#     "Employee_SirName":"Raut",
#     "Company_Name"    :"TCS",
#     "Designation"     :"Python & Development",
#     "Salary"          :1400000
#
#
# }

# student_name={"Name":"Rohit","Roll_no":56,"Marks":89,"Batch":2020}
# print(student_name.keys())
# print(student_name.values())
# print(student_name.items())

# Employee_Details={
#     "Employee_Name"   :"Prashant",
#     "Employee_SirName":"Raut",
#     "Company_Name"    :"TCS",
#     "Designation"     :"Python & Development",
#     "Salary"          :1400000
# }
# print(Employee_Details)
# Employee_Details["Employee_Name"]="Ankit"
# Employee_Details["Employee_SirName"]="patil"
# print(Employee_Details)



# di= {}
# di1 = dict()
# print(di,di1)

# di1={"keys1":"val1","keys2":"val2"}
# print(di1)
# print(di1.keys())
# print(di1.values())

di1={"keys1":"val1","keys2":"val2"}
# print(di1)
# print(di1.keys())
# print(di1.values())
# print(di1.items())
# print(di1["keys1"])
# print(di1["keys2"])
# print(di1.get("keys1"))
# for key in di1:
#     print(key)
# for values in di1.values():
#     print(values)
# for items in di1.items():
#     print(items)
#
# for key in di1:
#     print(di1[key])
#
# for key in di1:
#     print(di1["keys1"])

###08-04-2022

# stu_marks={
#     "Saurabh":88,
#     "Anuj"   :97,
#     "Sakhshi":87,
#     "Ankita":77
# }
# print(stu_marks)
# print(stu_marks["Saurabh"])
# stu_marks["Saurabh"]=55
# print(stu_marks)
# stu_marks["sakshi"]=67
# print(stu_marks)

# employee_database={
#     "Employee_Name":"Prashant",
#     "Company_Name" :"TCS",
#     "salary"       :60000,
#     "Designation"  :"Python_Developer"
# }
# print(employee_database)
# employee_database["location"]="Pune"
# print(employee_database)
# employee_database["Age"] = 265,
# employee_database["EMployee_Id"] = "ACD00516"
# employee_database["Address"]  = "Kolhapur"
# print(employee_database)

# employee_database = {
#     "Employee_Name" : "Prashant",
#     "Company_Name"  : "/TCS",
#     "Salary"        : 60000,
#     "Designation"   : "Python Developer"
# }
# new_data={
#     "Company_Location":"Mumbai",
#     "Age"             :30,
#     "Emp_Id"           : "CRD5563"
# }
# #print(employee_database)
# #print(new_data)
# employee_database.update(new_data)
# print(employee_database)

# d1 = {
#     "Emp_Name" : "Vaibhav",
#     "Company_Name" : "IOSTIO",
#     "Age"          :26
# }
#
# d2 = {
#     "Emp_Name" : "Suhas",
#     "Salary"   : 80000,
#     "Emp_Id"   : "ARD6652"
# }
# d1.update(d2)
# print(d1)
# d2.update(d1)
# print(d2)

###Deletion
# emp_db={
#     "emp_name"      :"suhas",
#     "Company_name"  :"TCS",
#     "Age"           :26,
#     'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# emp_db.pop("Age")
# print(emp_db)

# emp_db={
#     "emp_name"      :"suhas",
#     "Company_name"  :"TCS",
#     "Age"           :26,
#     'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# emp_db.popitem()
# print(emp_db)
# emp_db.popitem()
# print(emp_db)

# emp_db={
#     "emp_name"      :"suhas",
#     "Company_name"  :"TCS",
#     "Age"           :26,
#     'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# emp_db.clear()
# print(emp_db)

# emp_db={
#     "emp_name"      :"suhas",
#     "Company_name"  :"TCS",
#     "Age"           :26,
#     'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# del emp_db["Emp_Id"]
# print(emp_db)

# emp_db={
#     "emp_name"      :"suhas",
#     "Company_name"  :"TCS",
#     "Age"           :26,
#     'Emp_Id': 'ARD6652'
# }
# print(emp_db)
# del emp_db
# print(emp_db)


# stu_marks={}
# num_student=int(input("Enter how many student"))
# for i in range(num_student):
#     name=input("Enter name of student")
#     marks=float(input("Enter marks of student"))
#     stu_marks[name]=marks
# print(stu_marks)

# sq_li={}
# num=int(input("Enter the number"))
# for i in range(1,num+1):
#     square=i**2
#     sq_li[i]=square
# print(sq_li)

# upper_case={}
# for i in range(65,91):
#     upper_case[chr(i)]=i
# print(upper_case)


emp_db={
    "xyz1234":{
        "Emp_Name" :"Akash",
        "Emp_Age"  :27,
        "salary"   :90000,
        "Designation":"Python Developer"
    },
    "xyz1235":{
        "Emp_Name"   :"Sagar",
        "Emp_Age"    :26,
        "salary"     :[100000,20000,30000],
        "Designation":"Data Scientist"
    },
    "xyz1236":{
        "Emp_Name"   :"Prakash",
        "Emp_Age"    :30,
        "salary"     :700000,
        "Designation":"ML ENGG"
    },
}
print(emp_db)
# print(emp_db["xyz1235"])
# print(emp_db["xyz1235"]["Designation"])
# emp_db["xyz1235"]["Designation"]="AI Engg"
# print(emp_db["xyz1235"]["Designation"])
# print(emp_db["xyz1235"])
# print(emp_db["xyz1235"].keys())
# print(emp_db["xyz1235"].values())
# print(emp_db["xyz1235"].items())
# print(emp_db["xyz1235"]["salary"][1])
#
# for i in emp_db["xyz1235"]["salary"]:
#     print(i)

# print(emp_db["xyz1234"]["Designation"].split())
# print(emp_db)


# subject=["Phy","chem","math","Bio","Eng"]
# marks=[87,77,55,66,99]
# student_marks={}
# for i in range(len(subject)):
#     student_marks[subject[i]]=marks[i]
# print(student_marks)

# sub_marks = {'Phy': 87, 'Che': 77, 'Math': 55, 'Eng': 66, 'Bio': 99}
# print(sorted(sub_marks.keys(),reverse=True))

# sub_marks = {'Phy': 87, 'Che': 77, 'Math': 55, 'Eng': 66, 'Bio': 99}
# new_di = {}
# sor_keys = sorted(sub_marks.keys())
# for i in sor_keys:
#     new_di[i] = sub_marks[i]
# print(new_di)


##formkeys
# result=dict.fromkeys(list("ABCD"))
# print(result)
#
# result=dict.fromkeys(list("ABCD"),list("PQRS"))
# print(result)
#
# result=dict.fromkeys(list("ABCD"),99)
# print(result)
#
# result=dict.fromkeys("Python",99)
# print(result)

##setdefault
# sub_marks = {'Phy': 87, 'Che': 78, 'Math': 55, 'Eng': 66, 'Bio': 99}
# print(sub_marks.setdefault("Phy"))

# sub_marks = {'Phy': 87, 'Che': 78, 'Math': 55, 'Eng': 66, 'Bio': 99}
# print(sub_marks.setdefault("Physic",99))
# print(sub_marks)