# TODO: Initialize using dict keyword
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
# print(f"Chai Order: {chai_order}")

# TODO: Another way of initializing the dictionay
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# print(f"Recipe base: {chai_recipe['base']}")


# TODO: Delete
# print(f"Chai recipe: {chai_recipe}")
del chai_recipe["liquid"]
# print(f"Chai recipe: {chai_recipe}")


# TODO: Check Membership
# print(f"Is sugar in the order ? {"sugar" in chai_order}")


chai_order = {"type": "Ginger Chai", "Size": "Medium", "Sugar": 1}

# TODO: Printing Key and values
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")


# TODO: delete last item
# last_item = chai_order.popitem()
# print(f"Last Item: {last_item}")

# removed_item = chai_order.pop("Sugar")
# print(f"Removed item: {removed_item}")


# TODO: Update
extra_spices = {"cardamon": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated Chai recipe: {chai_recipe}")

# Get value safely: Like => Optionally accessig: .get()

customer_note = chai_order.get("customer_note", "NO NOTE")
print(f"Customer Note is: {customer_note}")
