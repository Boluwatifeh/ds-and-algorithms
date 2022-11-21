class Node:
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data
    def __repr__(self) -> str:
        return f"data in the node -> {self.data}"