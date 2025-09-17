# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0 

    def enqueue(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1 

    def dequeue(self):
        if self.is_empty():
            return None
        removed = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed.name
    
    def peek(self):
        return None if self.is_empty() else self.front.name 
    
    def is_empty(self):
        return self.front is None
    
    def __len__(self):
        return self.size 
    
    def __str__(self):
        current = self.front
        values = []
        while current:
            values.append(current.name)
            current = current.next
        return " -> ".join(values) if values else "(empty)"
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"Helped customer: {customer}")
            else:
                print("No customers waiting.")


        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers waiting.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            print(queue)
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
