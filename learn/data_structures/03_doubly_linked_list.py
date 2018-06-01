"""
03. Doubly Linked List: Nodes point to both next and previous elements.
This allows for bidirectional traversal of the list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()
