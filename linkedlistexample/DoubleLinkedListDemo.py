#We need to create Node class as our blueprint

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

#Create a class/blueprint for the DoubleLinkeList.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    #Add nodes to the Doubly Linked List
    def push(self, newValue):
        newNode = Node(newValue)

        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    #Insert method to insert node in a doubly linkedlist

    def insert(self, prevNode, newVal):

        if prevNode is None:
            return        
        newNode = Node(newVal)
        print("The newval to be inserted", newVal)
        newNode.next = prevNode.next #magiging kasunod na ni 13 si 8
        prevNode.next = newNode #magiging previous.next na ni 8 si 13
        newNode.prev = prevNode #previousNode ay equals na kay prevNode ngayon

        if newNode.next is not None:
            newNode.next.prev = newNode
    
     #Append method
    def append(self, newVal):

        newNode = Node(newVal)
        newNode.next = None #kaya sya None dahil sa hulihan na iaadd yung element/node
        if self.head is None:
            newNode.prev = None
            self.head = newNode #if ever na walng head value or starting point si newNode and magiging headval
            return
        
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    #Print the nodes
    def displayNode(self, node):
        while(node is not None):
            print(node.data),
            last = node
            node = node.next


student = DoublyLinkedList()

# student.push("Aljun")
# #Raniel
# student.push("Reymark")
# student.push("Danica")

student.push("Trixia")
student.push("Loen")

student.displayNode(student.head)

