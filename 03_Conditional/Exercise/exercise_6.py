"""
Food Menu Selector
You’re creating a menu price lookup system for a digital food ordering app using the match-case statement.

Tasks:
    - Define a function get_item_price that takes a string input item.
    - Use match-case to return the following based on the item name:
        "pizza" → "Price: 30 bucks"
        "burger" → "Price: 15 bucks"
        "pasta" → "Price: 20 bucks"
        "salad" → "Price: 10 bucks"
        Any other item → "Item not available"
Make sure the item check is case-insensitive (e.g., “BURGER” or “burger” should both match).
"""


def get_item_price(item: str) -> str:
    item = item.lower()
    match item:
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "rice: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"


item = input("Enter item: ")
selected_item_price = get_item_price("PIZZA")
print(f"SELECTED ITEM {item}: {selected_item_price}")
