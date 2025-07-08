# public member
class A:
    def hi(self):
        print("Hello i am public")
class B:
    def greet(self):
        print("Good Morning ")
        obja = A()
        obja.hi()
        print("*************************************")
objb = B()
objb.greet()

# protected member
class A:
    def _hi(self):
        print("Hello i am protected ")
class B(A):
    def greet(self):
        print("Good Morning ")
        obja = A()
        obja._hi()
        print("*************************************")
objb = B()
objb.greet()

# private member
class A:
    def __hi(self):
        print("Hello i am private")
    def access_hi(self):
        self.__hi()
class B(A):
    def greet(self):
        print("Good Morning ")

objb = B()
objb.greet()

obja = A()
obja.access_hi()
# cant call function hi from class a even from sub class or child class or through object