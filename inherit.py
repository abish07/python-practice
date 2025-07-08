# SINGLE INHERITANCE
# class parent:
#     def myproperty(self):
#         print("i am from parent class")
# class child(parent):
#     def property(self):
#         print("I am from child class")
# obj = child()
# print(obj.property())
# print(obj.myproperty())

# class CSIT:
#     university = "Tribhuwan University"
#     admissionFee = "100000"
#     def showDetails(self):
#         print(f"Our course can be available in multiple colleges")
# class SamriddhiCollege(CSIT):
#     def __init__(self):
#         self.issueDate = "1989 BS"
#         self.location = "Lokanthali"
#     def display(self):
#         print(f"University : {self.university}")
#         print(f"Admission Fee : {self.admissionFee}")
# obj= SamriddhiCollege()
# obj.display()
# obj.showDetails()


# MULTIPLE INHERITANCE
# class A:
#     A = "A"
# class B:
#     B = "B"
# class C(A,B):
#     def show(self):
#         print("I am class C")
#         print(f"Class {self.A} and class {self.B} are my parents")
# obj = C()
# obj.show()


# MULTILEVEL INHERITANCE
# class A:
#     A = "aaaaaaaaaaaaaaaaaaaaaa"
#     def showa(self):
#         print("I am from class A")
#         print()
# class B(A):
#     B = "bbbbbbbbbbbbbbbbbbbbbb"
#     def showb(self):
#         print("I am from class B")
#         print(f"I have the method or attribute of class A i.e {self.A}")
#         print()
# class C(B):
#     def showc(self):
#         print("I am from class C")
#         print(f"I have the method or attribute of class B i.e {self.B}")
#         print()
# obj = C()
# obj.showc()
# obj.showa()
# obj.showb()


# Heirarchial Inheritance
# class A:
#     A = "class A"
#     def show(self):
#         print("I am class A")
# class B(A):
#     def show(self):
#         super().show()
#         print(f"I am class B with the attribute of {self.A}")
# class C(A):
#     def show(self):
#         super().show()
#         print(f"I am class C with the attribute of {self.A}")
# class D(A):
#     def show(self):
#         super().show()
#         print(f"I am class D with the attribute of {self.A}")
# obj = D()
# obj.show()
    

# Hybbrid Inheritance
# class A:
#     A = "haha"
#     def show(self):
#         print("From class A: haha")
#         print()
# class B(A):
#     B = "hehe"
#     def show(self):
#         super().show()
#         print("From class B: hehe")
#         print(f"i have attribute of class A i.e {self.A}")
#         print()
# class C(A):
#     C = "huhu"
#     def show(self):
#         super().show()
#         print("From class C: hehe")
#         print(f"i have attribute of class A i.e {self.A}")
#         print()
# class D(B,C):
#     D = "hoho"
#     def show(self):
#         super().show()
#         print("From class D: hoho")
#         print(f"I have attribute of class A {self.A} , class B {self.B} and Class C {self.C}")
#         print()
# print(D.mro())
# obj = D()
# obj.show()