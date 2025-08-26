# Integer

black_tea_grams = 40
ginger_grams = 3
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of tea base: {total_grams}")


milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is: {milk_per_serving}")


# // => floor operator
# Returns the quotient rounded down (floored) to the nearest integer.
# Returns an integer (if both operands are integers)
# floored float (if any operand is float)

total_tea_bags = 7
pots = 4
bag_per_pots = total_tea_bags // pots
print(f"Whole tea bags per pots: {bag_per_pots}")


# % => modulo operator
# Gives the remainder of the division

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Lefetover Csdamon pods: {leftover_pods}")

# ** => power
print(2**3)


total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")