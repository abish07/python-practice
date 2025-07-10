# Built in Exception
# class Mathematics:
#     def division(self):
#         while True:
#             try:
#                 a = int(input("Enter the number-1 : "))
#                 b = int(input("Enter the number-2 : "))
#                 res = a/b
#                 if(b<0):
#                     raise Exception("cannot take a negative value")
#                 else:
#                     print(res)
#             except (ZeroDivisionError,ValueError) as obj:
#                 print(obj)
#             else:
#                 print(" i will be only there when the operation is Successfully operated")
#             finally:
#                 print("i will always be there")
#             break
# divide = Mathematics()
# divide.division()


#userdefined exception            
# class divideByFiveError(Exception):
#     pass

# try:
#     a = int(input("Enter the number-1 : "))
#     b = int(input("Enter the number-2 : "))
#     if(b==5):
#         raise divideByFiveError("Cannot divide a number by 5")
#     elif (b==7):
#         raise divideByFiveError("Cannot divide by seven")
#     else:
#         res = a/b
#         print(res)
# except Exception as obj:
#     print(obj)
# else:
#     print(" i will be only there when the operation is Successfully operated")
# finally:
#     print("i will always be there")

                
#Password Checker
# class invalidPassword(Exception):
#     pass
# storedPassword = "Cr7#united07"
# def login():
#     while True:
#         try:
#             password = input("Enter your password : ")
#             if(storedPassword == password):
#                 print("You are susseccfully logged in !!! ")
#             else:
#                 raise invalidPassword("Invalid Password!!! Please try again . ")
#         except invalidPassword as obj:
#             print("Password wrong : ",obj)
#         except Exception as e:
#             print("General error : ",e)
#         else:
#             print("Login Successful : ")
#             break
#         finally:
#             print("This is from Meta Account")

# login()