#ChatGPT used to quickly translate from original java version to python for this class
class GenericStack:
    def __init__(self):
        self.list = []

    def get_size(self):
        return len(self.list)

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        return None

    def push(self, o):
        self.list.append(o)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        return None

    def is_empty(self):
        return len(self.list) == 0
