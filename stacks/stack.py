class Stack:

    #create ng init method/constructor
    def __init__(self):
        self.stack = []
    

    #method to add data elements to the stack
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    #Which is the peek or the top element.
    def peek(self):
        return self.stack[-1]
    
    def remove(self):
        if len(self.stack) <=0:
            return "Empty Stacks. Cannot remove an element."
        else:
            return self.stack.pop()
    #view
    def view(self):
        return self.stack
    
#Create object of the Stack

stackStudent = Stack()


while True:
    choice = input('Enter your choice: ')

    if choice == "0":
        print("You exit.")
        break
    elif choice == '1':
        value = input("Enter the value you want to add: ")
        stackStudent.add(value)
        continue
    elif choice == '2':
        print(stackStudent.peek())
        continue
    elif choice == '3':
        stackStudent.remove()
        continue
    elif choice == '4':
        print(stackStudent.view())
        continue
    else:
        print("Invalid Input")
        break


