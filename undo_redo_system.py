# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node 
        self.size += 1 
    
    def pop(self):
        if self.is_empty():
            return None
        popped = self.topself.top = self.top.next
        self.size -= 1
        return popped.name 
    
    def peek(self):
        return None if self.is_empty() else self.top.name
    
    def is_empty(self):
        return self.top is None
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        current = self.top
        values = []
        while current:
            values.append(current.name)
            current = current.next
        return " -> ".join(values) if values else "(empty)"
    


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()


            print(f"Action performed: {action}")
        elif choice == "2":
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("Nothing to undo.")


            
            

        elif choice == "3":
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("Nothing to redo.")
            


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            print(undo_stack)
            
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:") 
            print(redo_stack)
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()