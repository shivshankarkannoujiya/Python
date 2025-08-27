chai_type = "Ginger Chai"
customer_name = "Ramam"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[0:8:1]}")
print(f"First word: {chai_description[0:8:2]}")
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[12:]}")

# Putting step Negative print reverse way
print(f"Reverse String: {chai_description[::-1]}")

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
print(f"Decoded label: {decoded_label}")
