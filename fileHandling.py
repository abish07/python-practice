#Write
# file = open("Readme.txt","w")
# file.write("Hello i am abish")
# file.close()

#Read
# file = open("Readme.txt","r")
# fileData = file.read()
# print(fileData)
# file.close()

#Append
# file = open("Readme.txt","a")
# file.write(" I am 20 Years Old")
# file.close()
import os
file = "haha.txt"
prohibitedLetter = "ERROR"
class EmptyFileError(Exception):
    pass
class ErrorKeywordFound(Exception):
    pass
try:
    if(os.path.exists(file)):
        with open(file,"r+") as file:
            readData = file.read()
            if(readData==""):
                raise EmptyFileError("File is Empty")
            elif prohibitedLetter in readData:
                raise ErrorKeywordFound("File contain the word Error")
            else:
                file.write("File Validated Successfully")
    else:
        raise FileNotFoundError("File not Found")
except FileNotFoundError as obj:
    print(obj)
except EmptyFileError:
    print("File is empty")
except ErrorKeywordFound:
    print(f"There is the presence of a word  {prohibitedLetter} in file")
else:
    print("Succssfully appended the validation text in the file")
