myStr = str(input("Enter any string to check weather it is palindrome or not: "))
myRevStr = myStr[::-1]

# using normal function
# def palindrome(myStr,myRevStr):
#     if(myStr == myRevStr):
#         return print("It is palindrome")
#     else:
#         return print("It is not palindrome")
# palindromeStr = palindrome(myStr , myRevStr)

# using lambda function
palindromStr = lambda x: "Palindrome" if(myStr==myRevStr) else "Not a palindrome"
print(palindromStr(myStr))