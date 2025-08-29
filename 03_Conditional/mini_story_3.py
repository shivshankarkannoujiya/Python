"""
A tea stall offers different prices for different cup sizes.
Write a program that calculate the price based on the size

Task
    - input: small, medium, large
    - small = 10
    - medium = 15
    - large = 20
    if invalid show:  "Unknown sup size"
"""

cup_size = input("Choose your cup size (small/medium/large): ").lower()

if cup_size == "small":
    print("Price is 10 rupees")
elif cup_size == "medium":
    print("Price is 15 rupees")
elif cup_size == "large":
    print("Price is 20 rupees")
else:
    print("Unknow cup size")
