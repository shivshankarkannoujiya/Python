ingredients = ["water", "milk", "black tea"]

# Add sugar to it 
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("water")
print(f"Ingredients are: {ingredients}")


# Extend the List
spice_options = ["ginger", "Cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")

# Add the value at particular postion 
chai_ingredients.insert(2 ,"Black Tea")
print(f"Chai: {chai_ingredients}")

# Remove value from particular position
last_added = chai_ingredients.pop()
print(f"Last added: {last_added}")


# Operator Overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid Mix: {full_liquid_mix}")

strong_brew = ["Black Tea"] * 3


strong_brew_2 = ["Black Tea", "water"] * 3
print(f"String Brew 2: {strong_brew_2}")

# String Charater ==> List
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")



