class Queue:
    def __init__(self):
        self.queue = list() #initializing the empty list, container
    
    def addtoq(self,dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            print("Data Elements Exists!")
    def size(self):
        return len(self.queue)
    
    def displayQueue(self):
        print(self.queue)
    
    def removefromq(self):
        if len(self.queue)>0:
            self.queue.pop() #removes the first element to arrive
        return print("No Elements in the Queue")

customerQueue = Queue()

while True:
    choice = int(input("Enter your Choice\n 1-Add \n 2-Get Size \n 3-Display the Queue\n 4-Remove From Queue\n>> "))
    if choice == 1:
        val = input("Enter the data element you want to add: ")
        customerQueue.addtoq(val)
        continue
    elif choice == 2:
        print(customerQueue.size())
        continue
    elif choice == 3:
        print(customerQueue.displayQueue())
        continue
    elif choice == 4:
        customerQueue.removefromq()
    else:
        print("Invalid Input")
        break

