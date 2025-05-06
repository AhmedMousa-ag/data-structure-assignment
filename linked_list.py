class Node:
    def __init__(self, data):
        self.data = data
        self.next:Node = None
        self.previous:Node = None  

    def __repr__(self):
        return f"Node({self.data})"
    
class DoublyLinkedList:
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None

    def __repr__(self):
        representative = ""
        node = self.head
        while node:
            representative += f"{node} <-> "
            node = node.next
        return representative.rstrip(" <-> ")
    
    def traverse_forward(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                break
            current_node = current_node.next
        return current_node
    
    def traverse_backward(self, data):
        current_node = self.tail
        while current_node:
            if current_node.data == data:
                break
            current_node = current_node.previous
        return current_node
    
    def insert_head(self, data):
        """Inserts data at the head"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head
        
        old_head = self.head
        new_node.next = old_head
        old_head.previous = new_node
        self.head = new_node
        return new_node
    
    def insert_end(self, data):
        """Inserts data at the tail"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return self.tail
        
        tail_node = self.tail
        tail_node.next = new_node
        new_node.previous = tail_node 
        self.tail = new_node
        return new_node
    
    def insert_after_node(self, after_node_data, data):
        after_node = self.traverse_forward(after_node_data)
        if after_node is None:
            # print(f"Node with data {after_node_data} not found")
            return None
            
        new_node = Node(data)
        
        # If inserting after the tail
        if after_node == self.tail:
            return self.insert_end(data)
            
        new_node.next = after_node.next
        new_node.previous = after_node
        
        if after_node.next:
            after_node.next.previous = new_node
        after_node.next = new_node
        
        return new_node
    
    def delete_node_forward(self, node_delete_data):
        """deletes item by traversing forward"""
        delete_node = self.traverse_forward(node_delete_data)
        if not delete_node:
            # print(f"Node with data {node_delete_data} not found")
            return None
            
        # If deleting the head
        if delete_node == self.head:
            self.head = delete_node.next
            if self.head:
                self.head.previous = None
            else:
                # If list becomes empty
                self.tail = None
            return
            
        # If deleting the tail
        if delete_node == self.tail:
            self.tail = delete_node.previous
            self.tail.next = None
            return
            
        # If deleting a middle node
        delete_node.previous.next = delete_node.next
        delete_node.next.previous = delete_node.previous

    def delete_node_backward(self, node_delete_data):
        """deletes item by traversing forward"""
        delete_node = self.traverse_backward(node_delete_data)
        if not delete_node:
            # print(f"Node with data {node_delete_data} not found")
            return None
            
        # If deleting the head
        if delete_node == self.head:
            self.head = delete_node.next
            if self.head:
                self.head.previous = None
            else:
                # If list becomes empty
                self.tail = None
            return
            
        # If deleting the tail
        if delete_node == self.tail:
            self.tail = delete_node.previous
            self.tail.next = None
            return
            
        # If deleting a middle node
        delete_node.previous.next = delete_node.next
        delete_node.next.previous = delete_node.previous
   
if __name__ == "__main__":
    doubly_list = DoublyLinkedList()
    doubly_list.insert_head(1)
    print(f"{doubly_list}")
    
    doubly_list.insert_end(3)
    print(f"{doubly_list}")
    
    doubly_list.insert_after_node(1, 2)
    print(f"{doubly_list}")
    
    doubly_list.delete_node(2)
    print(f"{doubly_list}")