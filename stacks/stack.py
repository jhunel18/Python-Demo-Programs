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
product  = Stack()
price = Stack()

while True:

    choice = int(input("Enter your choice: "))
    if choice == 1:
        prod = input("Ente the product ")
        p = float(input("Enter the price: "))

        product.add(prod)
        price.add(p)
    elif choice == 2:
        print(product.view())
        print(price.view())
    
    elif choice == 3:
        product.remove()
        price.remove()
    