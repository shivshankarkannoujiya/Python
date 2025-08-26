spice_mix = set()

print(f"Initial spice_mix iD: {id(spice_mix)}") #1795312083552
print(f"Initial spice_mix iD: {spice_mix}") 
spice_mix.add("Ginger")
spice_mix.add("Cardmon")
print(f"After Initial spice_mix iD: {id(spice_mix)}") #1795312083552
print(f"After Initial spice_mix iD: {spice_mix}") 

# ID remains same after adding : MUTABLE
# 1795312083552
# 1795312083552

