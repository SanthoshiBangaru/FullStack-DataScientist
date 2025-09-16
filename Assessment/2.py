# 2. Restaurant Menu Management 
def add_item(menu, item):
    if item not in menu:
        menu.append(item)
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in menu.")
    return menu

def check_item(menu, item):
    return f"{item} is available" if item in menu else f"{item} is not available"


if __name__ == "__main__":
    menu = ["Pizza", "Burger", "Pasta", "Salad"]
    menu = add_item(menu, "Tacos")
    menu = remove_item(menu, "Salad")
    print("Updated menu:", menu)
    print("Availability:", check_item(menu, "Pizza"))