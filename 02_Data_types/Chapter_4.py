is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # upcasting
print(f"total actions : {total_actions}")


# Logical operators

is_water_hot = True
is_tea_added = False

can_serve = is_water_hot and is_tea_added
print(f"Can server chai: {can_serve}")
