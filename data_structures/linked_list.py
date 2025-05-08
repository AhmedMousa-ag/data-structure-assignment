class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        # Optional, will not always be used based on the type of the Linked List.
        self.previous: Node = None

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        representative = ""
        node = self.head
        while node:
            representative += f"{node} -> "
            node = node.next
        return representative.rstrip(" -> ")

    def traverse(self, data):
        """Traverses the list to find a node with the given data"""
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def insert_head(self, data):
        """Inserts data at the head"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self.head

        new_node.next = self.head
        self.head = new_node
        return new_node

    def insert_end(self, data):
        """Inserts data at the tail"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return self.tail

        self.tail.next = new_node
        self.tail = new_node
        return new_node

    def insert_after_node(self, after_node_data, data):
        """Inserts data after a node with the given data"""
        after_node = self.traverse(after_node_data)
        if after_node is None:
            return None

        new_node = Node(data)

        # If inserting after the tail
        if after_node == self.tail:
            return self.insert_end(data)

        new_node.next = after_node.next
        after_node.next = new_node

        return new_node

    def delete_node(self, node_data):
        """Deletes the node with the given data"""
        if not self.head:
            return None

        # If deleting the head
        if self.head.data == node_data:
            self.head = self.head.next
            # If list becomes empty
            if not self.head:
                self.tail = None
            return

        # Find the node before the one to delete
        current = self.head
        while current.next and current.next.data != node_data:
            current = current.next

        # If the node to delete was not found
        if not current.next:
            return None

        # If deleting the tail
        if current.next == self.tail:
            self.tail = current

        # Delete the node
        current.next = current.next.next


class DoublyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

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
            print(current_node)
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def traverse_backward(self, data):
        current_node = self.tail
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.previous
        return None

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
        self.delete_node(delete_node)

    def delete_node_backward(self, node_delete_data):
        """deletes item by traversing forward"""
        delete_node = self.traverse_backward(node_delete_data)
        self.delete_node(delete_node)

    def delete_node(self, delete_node: Node):
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


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if not self.head:
            return ""

        representative = ""
        node = self.head

        # First node
        representative += f"{node} -> "
        node = node.next

        # Rest of the nodes until we reach head again
        while node and node != self.head:
            representative += f"{node} -> "
            node = node.next

        # Show the circular nature
        representative += "..."
        return representative

    def traverse(self, data):
        """Traverses the list to find a node with the given data"""
        if not self.head:
            return None

        current_node = self.head

        # Check the first node
        if current_node.data == data:
            return current_node

        current_node = current_node.next

        # Check the rest of the nodes until we reach head again
        while current_node and current_node != self.head:
            if current_node.data == data:
                return current_node
            current_node = current_node.next

        # If we reach here, the node was not found
        return None

    def traverse_full_cycle(self):
        if not self.head:
            return None
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def insert_head(self, data):
        """Inserts data at the head"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            # Make it circular
            new_node.next = new_node
            return new_node

        # Connect new node to head and tail
        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

        return new_node

    def insert_end(self, data):
        """Inserts data at the tail"""
        if not self.head:
            return self.insert_head(data)

        new_node = Node(data)

        # Connect new node to head and update tail
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def insert_after_node(self, after_node_data, data):
        """Inserts data after a node with the given data"""
        after_node = self.traverse(after_node_data)
        if not after_node:
            return None

        new_node = Node(data)

        # If inserting after the tail
        if after_node == self.tail:
            return self.insert_end(data)

        new_node.next = after_node.next
        after_node.next = new_node

        return new_node

    def delete_node(self, node_data):
        """Deletes the node with the given data"""
        if not self.head:
            return None
        # Case 1: Only one node in the list
        if self.head == self.tail:
            if self.head.data == node_data:
                self.head = None
                self.tail = None
            return

        # Case 2: Deleting the head
        if self.head.data == node_data:
            self.head = self.head.next
            self.tail.next = self.head
            return

        # Case 3: Deleting a node that's not the head
        current = self.head
        while current.next != self.head and current.next.data != node_data:
            current = current.next

        # If the node was not found
        if current.next == self.head:
            return None

        # If deleting the tail
        if current.next == self.tail:
            self.tail = current

        # Delete the node
        current.next = current.next.next
