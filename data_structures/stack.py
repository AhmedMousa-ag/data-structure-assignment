from data_structures.linked_list import DoublyLinkedList


class StackArrayBased:
    def __init__(self):
        self.size=-1
        self.stack=[]

    def __repr__(self):
        return str(self.stack)
    
    def push(self,data):
        self.stack.insert(0,data)
        self.size +=1
        return self.stack
    
    def pop(self):
        if self.size<1:
            return None
        item = self.stack[0]
        del self.stack[0]
        return item
    
    def search(self,data):
        for idx,item in enumerate(self.stack):
            if item==data:
                return idx
        return None
class StackLinkedList:
    def __init__(self):
        self.stack = DoublyLinkedList()

    def __repr__(self):
        return str(self.stack)
    
    def push(self,data):
        self.stack.insert_head(data)
        return self.stack
    
    def pop(self):
        item = self.stack.head
        if item is None:
            return None
        self.stack.delete_node_forward(item.data)
        return item
    
    def search(self,data):
        return self.stack.traverse_forward(data)