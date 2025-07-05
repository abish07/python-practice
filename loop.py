n = int(input("Enter any series of number"))
mul = 1
i= 1
# num = n
# rev =0 
# while(n!=0):
#     remainder = n%10
#     rev = rev *10 + remainder
#     n = n//10
# print(rev)  
# if(num==rev):
#     print("Palindrome")
# else:
#     print("Not palindrome")

while (i<=10):
    mul = n*i
    print(f"{n} * {i} = {mul}")
    i+=1
