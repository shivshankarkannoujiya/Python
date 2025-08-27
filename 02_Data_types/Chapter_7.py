masala_spices = ("cardamom", "cloves", "cinamon")

# Unpacking
(spice1, spice2, spice3) = masala_spices
print(f"Printing tuples: {masala_spices}")
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")


ginger_ratio, cardamon_ratio = 2, 1
# ginger_ratio = 2
# cardamon_ratio = 1
"""
- Behind the scene it is possible due to the: tuple
"""
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")

# Flip the values
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardamon_ratio}")

# MEMBERSHIP: string in <where to check>: it is case_sensitive
print(f"Is ginger in masala spices ? {"ginger" in masala_spices}")


