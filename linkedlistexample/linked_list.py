class Node:

    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:

    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    #Add data at the beginning
    def atBeginning(self, newdata):
        #set the new element as the head or the starting
        NewNode = Node(newdata)

        #Update the new nodes nextval to existing code
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    #add element at end
    def atEnd(self, newdata):

        NewNode = Node(newdata)

        if self.headval is None:
            self.headval = NewNode
            return
        lastVal = self.headval

        while(lastVal.nextval):
            lastVal = lastVal.nextval
        lastVal.nextval = NewNode
    
    #To add element at the middle
    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The node is absent")
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    
    #To Remove data element
    def RemoveNode(self, RemoveKey):

        HeadVal = self.headval
        print("Headval value: ", HeadVal)

        if(HeadVal is not None):
            self.head = HeadVal.nextval
            HeadVal = None
            return
        while(HeadVal is not None):
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if(HeadVal == None):
            return
        prev.next = HeadVal.next

        HeadVal = None
            


llist = SLinkedList()
e1 = Node("Sun")
llist(e1)
llist.atBeginning("Mon")
llist.atBeginning("Tue")
llist.atBeginning("Wed")
llist.atBeginning("Tue")

llist.RemoveNode("Tue")
llist.listprint()