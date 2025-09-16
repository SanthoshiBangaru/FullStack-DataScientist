# 1. E-Commerce Cart System
def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty"

    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total *= 0.9 

    return total

if __name__ == "__main__":
    cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
    print("Total Price:", calculate_total(cart_items))
