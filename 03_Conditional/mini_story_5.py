"""
You run an onlne tea store

if the order amount is more than Rs 300, delivery is free,
Otherwise, it cost Rs 30

Task:
    - input: order_amount
    - Use ternary oerator to decide delivery fee
"""

order_amount = int(input("Enter your order amount: "))

delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees is: {delivery_fees}")
