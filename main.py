from data_structures.stack import StackLinkedList
from data_structures.queue import QueueLinkedBased

class Item:
    def __init__(self,name:str,price:float):
        self.name=name
        self.price=price
    def __repr__(self):
        return f"name: {self.name} , price: {self.price}"

if __name__=="__main__":
    # Stack implementation
    wish_cart = StackLinkedList()
    # If a user puts an item to purchase card.
    wish_cart.push(Item("Book",19.0))
    print(f"User wish cart: {wish_cart}")
    wish_cart.push(Item("TV",400.0))   
    print(f"User wish cart: {wish_cart}")
    # The user wants to add another item.
    wish_cart.push(Item("Ball",1.5))
    print(f"User wish cart: {wish_cart}")
    print("\n")
    # When the user wants to pay for their order to be delivered.
    order_process = QueueLinkedBased()
    item_to_process = wish_cart.pop()
    while item_to_process:
        print(f"Registered item: {item_to_process.data} to be delivered to the user.")
        order_process.enqueue(item_to_process)
        item_to_process = wish_cart.pop()
        
    print("\n")
    # Now time to deliver
    item_to_deliver = order_process.dequeue()
    while item_to_deliver:
        print(f"Dilvered item: {item_to_deliver}")
        item_to_deliver = order_process.dequeue()

    