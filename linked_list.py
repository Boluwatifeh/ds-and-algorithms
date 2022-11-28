class Node:
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data
    def __repr__(self) -> str:
        return f"data in the node -> {self.data}"

class Linkedlist:

    def __init__(self):
        self.head = None 
    
    def is_empty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0 
        while current != None:
            count += 1
            current = current.next_node
        return count
    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"Head: {current.data}")
            elif current.next_node is None:
                nodes.append(f"Tail: {current.data}")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node
        return "-".join(nodes)
