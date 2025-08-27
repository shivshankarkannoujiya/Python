# Real Number: mean i want precision in my programming
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temperature = 95.5
current_temperature= 95.49999999

print(f"ideal temp: {ideal_temperature}")
print(f"current temp: {current_temperature}")
print(f"diff temp: {ideal_temperature - current_temperature}")
print(sys.float_info)

