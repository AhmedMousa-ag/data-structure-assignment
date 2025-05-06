from data_structures.stack import StackLinkedList
from data_structures.queue import QueueLinkedBased


if __name__=="__main__":
    wish_cart = StackLinkedList()
    # If a user puts an item to purchase card.
    wish_cart.push("Book")
    print(f"User wish cart: {wish_cart}")
    wish_cart.push("TV")   
    print(f"User wish cart: {wish_cart}")
    # The user wants to add another item.
    wish_cart.push("Ball")
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

