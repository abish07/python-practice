class stack:
    def __init__(self,size):
        self.size = size
        self.top=-1
        self.stack=[None]*size
    
    def push(self,items):
        if(self.top==self.size-1):
            print("Stack Overflow")
        else:
            self.top+=1
            self.stack[self.top]=items
            print(f"{items} is pushed into the stack")
    def pop(self):
        if(self.top==-1):
            print("Stack Underflow")
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -=1
            print(f"{temp} is popped from the stack")
    def peek(self):
        if self.top==-1:
            print(f"Stack Underflow")
        else:
            print(f"{self.stack[self.top]} is the present in the stack top")
    def display(self):
        if self.top==-1:
            print("Underflow")
        else:
            print("The items present in the stack is")
            print()
            for i in range(self.top,-1,-1):
                print(self.stack[i])

def main():
    size = int(input("Enter the size of the stack"))
    s = stack(size)


    while True:
        print("1. Push Operation")
        print("2. Pop Operation")
        print("3. Peek Operation")
        print("4. Display Operation")
        print("5. Exit")
        choice = input("Enter the choices to perform in the data structure")
        match choice:
            case '1':
                value = input("Enter the value to push")
                print(s.push(value))
            case '2':
                print(s.pop())
            case '3':
                print(s.peek())
            case '4':
                print(s.display())
            case '5':
                break
            case _:
                print("Invalid choice")
                break
main()