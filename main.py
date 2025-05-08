from data_structures.stack import StackLinkedList
from data_structures.queue import QueueLinkedBased
from data_structures.linked_list import CircularLinkedList, Node
import random

if __name__ == "__main__":
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
    delivery_status = CircularLinkedList()
    # Now time to deliver
    item_to_deliver: Node = order_process.dequeue()
    while item_to_deliver:
        delivery_status.insert_head(item_to_deliver.data)
        if random.randint(1, 10) < 5:  # 50% chance delivery
            delivery_status.delete_node(item_to_deliver.data)
            print(f"Dilvered item: {item_to_deliver.data}")
        item_to_deliver = order_process.dequeue()
    not_delivered = next(delivery_status.traverse_full_cycle())
    while not_delivered:
        if random.randint(1, 10) < 9:  # 90% chance delivery
            print(f"Deliverd Item: {not_delivered.data}")
            delivery_status.delete_node(not_delivered.data)
            try:
                not_delivered = next(delivery_status.traverse_full_cycle())
            except:
                print(f"Delivered all items....")
                not_delivered = None
