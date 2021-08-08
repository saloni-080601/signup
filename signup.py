import re
import json
import os
file_exist=os.path.exists("signup.json")
print(file_exist)
if file_exist==False:
    dic3={}
    list3=[]
    dic4={}
    user=input("enter a signup/login")
    if user == "s":
        num1=input("enter a name")
        num5=input("enter a password")
        if re.search("[A-Z]",num5) and re.search("[a-z]",num5) and re.search("[0-9]",num5) and re.search("[@#$%^&*!]",num5):
            num6=input(" conform password ")
            if num5==num6:
                print("password is correct")
                description=input("enter a description")
                birth=input("enter a birth of date")
                hobby=input("enter a hobby")
                Gender=input("enter a Gender F/M")
                list1=["Name","Password","describtion","Birth Of Date","Hobby","Gender"]
                list2=[num1,num5,description,birth,hobby,Gender,]
                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3.append(dic3)
                dic4.update({"user":list3})
                with open("signup.json","w") as h:
                    json.dump(dic4,h,indent=3)
        else:
            print("enter Capital letter, small letter, special character(!@#$$) and numbers")       
    
elif file_exist==True:
    dic3={}
    list2=[]
    dic4={}
    user=input("enter a signup/login")
    if user == "s":
        num1=input("enter a name")
        num5=input("enter a password")
        with open("signup.json","r") as f:
                data=json.load(f)
        if re.search("[A-Z]",num5) and re.search("[a-z]",num5) and re.search("[0-9]",num5) and re.search("[@#$%^&*!]",num5):
            num6=input(" conform password ")
            if num5==num6:
                print("password is correct")
                description=input("enter a description")
                birth=input("enter a birth of date")
                hobby=input("enter a hobby")
                Gender=input("enter a Gender F/M")
                list1=["Name","Password","describtion","Birth Of Date","Hobby","Gender"]
                list2=[num1,num5,description,birth,hobby,Gender,]
                for i in range(0,len(list1)):
                    dic3.update({list1[i]:list2[i]})
                list3=[]
                list3.append(dic3)
                data.update({"user":list3})
                with open("signup.json","w") as h:
                    json.dump(data,h,indent=3)
        else:
            print("enter Capital letter, small letter, special character(!@#$$) and numbers")  
    elif user=="l":
        user_name=input("Enter a name")
        user_password=input("enter a password")
        with open("signup.json","r") as data:
            u=json.load(data)
        for i in u:
            if i==user_password:
                print("right")
                print(u[i])

        else:
            print("wrong")
         
    
    #     else:
    #         print("enter Capital letter, small letter, special character(!@#$$) and numbers")
    # elif user=="l":
    #     user_name=input("Enter a name")
    #     user_password=input("enter a password")
    #     sub=open("signup.json","r")
    #     u=json.load(sub)
    #     print(u)
    #     for i in u:
    #         if i==user_password:
    #             print("right")
    #             print(u[i])
    #         else:
    #             print("wrong password")