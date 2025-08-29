"""
You are building a ticket info system for a railway app
Based on seat type, show its features.

Task: 
    - Input: "sleeper", "AC", "general", "luxury"
    - Match using match-case
    - Unknown: show invalid seat type
"""

train_seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match train_seat_type:
    case "sleeper":
        print("Sleeper -> NO AC")
    case "ac":
        print("AC - Air Condition, comfy ride")
    case "general":
        print("General - Cheapest option")
    case "luxury":
        print("Luxury - Premium seats and meals")
    case _:
        print("Invalid seat type")
