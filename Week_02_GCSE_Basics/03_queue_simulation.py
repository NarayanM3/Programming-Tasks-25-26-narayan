"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.
"""

class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, customer):
        self.items.append(customer)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def peek(self):
        if len(self.items) > 0:
            return self.items[0]

    def size(self):
        return len(self.items)


def main():
    myQueue = queue()

    while True:
        customer = input("Enter customer name (or 'q' to quit): ")
        if customer.lower() == 'q':
          break

        myQueue.enqueue(customer)

    while myQueue.size() > 0:
        print("Next customer: ", myQueue.peek())
        print(myQueue.dequeue(), " has been served.")
        print("Customers left: ", myQueue.size())

if __name__ == "__main__":
    main()
