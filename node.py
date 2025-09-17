# Implement your Node class here
class Node:

    def __init__(self, name, next=None):
        self.name = name
        self.next = next
    
    def __repr__(self):
        return f"Node({self.name})"