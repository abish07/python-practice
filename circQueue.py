class Queue:
    def __init__(self,size):
        self.size = size
        self.queue=[None]*size
        self.front = -1
        self.rear = -1
    def enqueue(self,items):
        if self.rear==self.size-1:
            print("Queue is full")
        else:
            if self.front==-1:
                self.front=0
            self.rear+=1
            self.queue[self.rear]=items
            print(f"{items} is pushed into the queue")
    def dequeue(self):
        if (self.rear==-1 or self.front==-1 or self.front>self.rear):
            print("Queue is empty")
        else:
            removed=self.queue[self.front]
            self.queue[self.front]=None
            self.front+=1
            print(f"{removed} is deleted from the queue")
            if self.queue[self.front]:
                self.rear=self.front=-1
    def peek(self):
        if self.rear==-1 or self.front==-1 or self.front>self.rear:
            print("Queue is empty")
        else:
            print(f"{self.queue[self.front]} is the first value from the queue")
    def display(self):
        if self.rear==-1 or self.front==-1 or self.front>self.rear:
            print("Queue is empty")
        else:
            print("The items present in the queue are: \n")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end="")
                print()

    def sum_even_number_in_queue(self):
        sum=0
        for i in range(self.front,self.rear+1):
            # evenList = list(self.queue[i]%2==0)
            # sum(evenList)
            print()
            if(self.queue[i]%2==0):
                sum+=self.queue[i]
        print(f"sum is {sum}")
            
def main():
    
    size=int(input("Enter the size of the queue"))
    s=Queue(size)
    while True:
        print("Queue operations !!")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. display")
        print("5. Exit")
        print("6. sum")
        choice=input("Enter the choice to perform : ")
        if(choice=='1'):
            value=int(input("Enter the value to enqueued"))
            s.enqueue(value)
        elif(choice=='2'):
             s.dequeue()
        elif(choice=='3'):
             s.peek()
        elif(choice=='4'):
             s.display()
        elif(choice=='5'):
             break
        elif(choice=='6'):
            s.sum_even_number_in_queue()
        else:
            print("Invalid choice!!! please select the valid choice")
if __name__=='__main__':
    main()
            
        
