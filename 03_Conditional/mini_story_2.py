"""
A local cafe wants a program that suggest the snacks.
if Customer ask for cookies or Samosa it confirm the order, otherwise it says it is not availbale

Task: 
    - Take Snacks input
    - if "cookies" or "samosa" confirm the order
    - Else, Show Unavailability 
"""

snacks = input("Enter snacks you want to order: ").lower()
print(f"User said: {snacks}")

if snacks == "cookies" or snacks == "samosa":
    print(f"Great! We will serve you {snacks}")
else:
    print("Sorry! we we only serve cookies and samosa with chai")
