import math

# for x in range(1,n+1):
#     fact*=x
# print(fact)

# while(i<=n):
#     prod*=i
#     i+=1

# print(prod)

# Normal function
def factorial(num):
    fact=1
    for x in range(1,n+1):
        fact*=x
    return fact


# recursive function
def recursiveFact(num):
    if (num==1 or num ==0):
        return 1
    else:
        return num*recursiveFact(num-1)

# lambda function
facto = lambda x: x if(x<=1) else x*facto(x-1)

while(1):
    print("1. Using Normal Function")
    print("2. Using Recursive Function")
    print("3. Using Lambda Function")
    print("4. Using Module Function")

    key = int(input("Select the number"))
    match key:
        case 1:
            n=int(input("Enter any number for normal function : "))
            print(factorial(n))
            break
        case 2:
            n1=int(input("Enter another number for recursive function : "))
            print(recursiveFact(n1))
            break
        case 3:
            n2=int(input("Enter another number for lambda function : "))
            print(facto(n2))
            break
        case 4:
            n3=int(input("Enter another number for module : "))
            print(math.factorial(n3))
            break
        case _:
            print("Milena")
            break