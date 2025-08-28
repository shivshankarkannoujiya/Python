essential_spices = {"cardamom", "ginger", "cinamon"}
optional_spices = {"cloves", "ginger", "black paper"}

# Union: |
all_spices = essential_spices | optional_spices
print(f"All SPICES: {all_spices}")

# Intersection: &
common_spices = essential_spices & optional_spices
print(f"COMMON SPICES: {common_spices}")

# Differences
only_in_essential = essential_spices - optional_spices
print(f"ONLY IN ESSENTIAL SPICES: {common_spices}")

# Check Membership
print(f"Is cloves in optional spices ? {"cloves" in optional_spices}")

# frozenset