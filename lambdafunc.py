# # number = int(input("Enter your marks: "))
# # if(number>0):
# #     print("The number is Positive")
# # elif(number<0):
# #     print("The number is Negative")
# # else:
# #     print("The number is Zero")


# # marks = lambda x:"First Divison" if(x>80 and x<=100) else("Second Division" if (x>60 and x<=80) else("Third Division" if (x>50 and x<=60) else("Forth division" if(x>40 and x<=50) else("Fifth division" if(x>=30 and x<=40) else "Fail"))))
# # print(marks(number))

# #list
# list= ["apple", "banana","cherry"]
# name=["Abish", "Krishom", "Nabin"]
# # lsit allows{duplicate values,
# #             are mutable,
# #             takes multiple datatype,
# #             are ordered,
# #             are heterogeneous
# # print(list[-2:-1]) #Excessing a List
# for i in range(len(list)):
#     print(f"{name[i]}  {list[i]}")

# tropical = ["mango","pineapple","papaya"]
# list.extend(tropical)

# list.sort(reverse=True)
# print(list)

def myfunc(n):
    return abs(n-50)
thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)