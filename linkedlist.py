class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current  
            current = current.next
        return None 
linked_list = LinkedList()
values = [5, 3, 6, 1, 0]
for value in values:
    linked_list.add(value)
search_value = 1
result_node = linked_list.search(search_value)
if result_node:
    print(f"Node {result_node.data}")
else:
    print("Null")