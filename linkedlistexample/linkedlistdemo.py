class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None


#Class for LinkedList
class LinkedList:
    def __init__(self):
        self.headval = None
    
    def display(self):
        printval = self.headval
        while printval is not None:
            print((printval.dataval))
            printval = printval.nextval
    
    #Method to insert a node atBeginning

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

        #Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    #Insert at the End of the given linked list

    def AtEnd(self, newdata):
        NewNode = Node(newdata)

        if self.headval is None:
            self.headval = NewNode
            return

        lastVal = self.headval
        while(lastVal.nextval):
            lastVal = lastVal.nextval
        lastVal.nextval=NewNode

    #Insert Between two nodes

    def InBetween(self, middle_node, newdata):

        if middle_node is None:
            print("The node is not existing")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    #Remove method to remove items in a linked list

    def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if(HeadVal is not None):
            if(HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while(HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if(HeadVal == None):
            return
        
        prev.nextval = HeadVal.nextval
        HeadVal = None



#Create an instance/object from the the LinkedList
daysLinkedList = LinkedList()

#create an instance/object of Node

e1 = Node("Mon")

#Assign a head or starting to our linked list
daysLinkedList.headval=e1

e2 = Node("Tue")
e3 = Node("Wed")
#link first node to the second node
daysLinkedList.headval.nextval = e2
#linked the second node e2 to third node e3
e2.nextval=e3
daysLinkedList.RemoveNode("Wed")
#print the data elements
daysLinkedList.display()