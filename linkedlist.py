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
                return "Node"
            current = current.next
        return "Null"
linked_list = LinkedList()
values = [5, 3, 6, 1, 0]
for value in values:
    linked_list.add(value)
search_value = 6
result = linked_list.search(search_value)
print(result)