"""
You are building a smart thermostat alert system
- if the divice_status is "active"
    - And temperature > 35 -> Warn: High temperature alert!
    - Else Temperature Normal
- if device is off -> "Device is offline" 
"""

device_status = input("Enter status: ").lower()
temperature = int(input("Enter temperature: "))

if device_status == "active":
    if temperature > 35:
        print("WARN:High temperature alert!")
    else:
        print("Temperature Normal")
else:
    print("Device is offline")
