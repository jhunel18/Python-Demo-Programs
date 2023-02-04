#Create the blueprint for the Node

class Node:
    def __init__(self, data):
        #data
        self.data = data
        #reference point to the previous
        self.prev = None
        #reference point to the next node
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        #starting point or head value
        self.head = None
    
    def push(self, newVal):

        newNode = Node(newVal)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    def display(self, node):
        
        while(node is not None):
            print(node.data)
            last = node
            node = node.next
    
    def insert(self, prev_node, newVal):

        if prev_node is not None:
            return
        
        newNode = Node(newVal)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node

        if newNode.next is not None:
            newNode.next.prev = newNode



student = DoublyLinkedList()

student.push("Aljun")
student.push("Reymark")
student.push("Danica")

#insert method

student.insert(student.head.next, "Raniel")
student.display(student.head)

