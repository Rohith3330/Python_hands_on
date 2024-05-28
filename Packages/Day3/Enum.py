from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    PREPARING = 3
    OUT_FOR_DELIVERY = 4
    DELIVERED = 5
    CANCELLED = 6

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = OrderStatus.PENDING

    def update_status(self, new_status):
        if new_status == OrderStatus.CANCELLED:
            print("Order cancelled.")
        elif new_status == OrderStatus.DELIVERED:
            print("Order delivered.")
        elif new_status == OrderStatus.OUT_FOR_DELIVERY:
            print("Order is out for delivery.")
        elif new_status == OrderStatus.PENDING:
            print("Order is pending.")
        elif new_status == OrderStatus.PREPARING:
            print("Order is being prepared.")
        elif new_status == OrderStatus.CONFIRMED:
            print("Order confirmed.")
        else:
            print("Invalid status.")
        
        self.status = new_status

# Example usage:
def main():
    order = Order(order_id="12345")
    print(f"Current Order Status: {order.status}")  

    while True:
        new_status_str = input("Enter new status (or 'exit' to quit): ").upper()
        if new_status_str == "EXIT":
            break
        
        try:
            new_status = OrderStatus[new_status_str]
            order.update_status(new_status)
        except ValueError:
            print("Invalid status. Please enter a valid status or 'exit'.")

    print(f"Order status updated. Final Status: {order.status}")
if __name__ == "__main__":
    main()