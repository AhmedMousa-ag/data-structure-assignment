from linked_list import DoublyLinkedList


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
        self.stack.delete_node_forward(item.data)
        return item

if __name__=="__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)