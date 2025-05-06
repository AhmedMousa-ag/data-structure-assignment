"""This file implements Queues in Python"""
from data_structures.linked_list import DoublyLinkedList
class QueueArrayBased:
    def __init__(self):
        self.size=-1 #Start the size from -1 as first item is indexed zero 
        self.queue=[]

    def __repr__(self):
        return str(self.queue)
    
    def enqueue(self,item):
        #Increase the size of the array by one.
        self.size+=1
        #Assign the item at the rear of the list.
        self.queue.append(item)
        # Return the queu
        return self.queue
    
    def dequeue(self):
        # Check if the array is empty or not, I choose to keep track of the array size in a variable for speed performace reasons.
        if self.size<1:
            return None
        # Get the first item in the queue
        item = self.queue[0]
        # Update the queue to include all the items except the first item which we just removed. It can also be used using pop.
        del self.queue[0]
        # Decrease the size of the array.
        self.size-=1
        # Return the first item
        return item
    


class QueueLinkedBased:
    def __init__(self):
        self.size=0 # type: ignore
        self.queue=DoublyLinkedList()

    def __repr__(self):
        return str(self.queue)
    
    def enqueue(self,item):
        self.queue.insert_end(item)
        # Return the queu
        return self.queue
    
    def dequeue(self):
        item=self.queue.head.data
        self.queue.delete_node_forward(item)
        return item



if __name__=="__main__":
    # queue = QueueArrayBased()
    queue = QueueLinkedBased()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.dequeue())
    print(queue)