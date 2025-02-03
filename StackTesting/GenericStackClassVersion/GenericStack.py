#ChatGPT used to quickly translate from original java version to python for this class
class GenericStack:
    def __init__(self):
        self.list = []  # Initialize an empty list to store stack elements
    
    def get_size(self):
        return len(self.list)  # Return the size of the stack (equivalent to list.size())
    
    def peek(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.list[-1]  # Return the last item (top of the stack)
        return None  # Return None if the stack is empty
    
    def push(self, o):
        self.list.append(o)  # Add an item to the top of the stack (list.add())
    
    def pop(self):
        o = self.list[-1]  # Get the top item
        self.list.pop()  # Remove the top item (list.remove())
        return o  # Return the popped item
    
    def is_empty(self):
        return len(self.list) == 0  # Check if the stack is empty (list.isEmpty())
