
#Assignment 4 (Static Inventory Management Using Only Dictionary)

inventory = {
    "pen": {"price": 10, "qty": 50},
    "book": {"price": 120, "qty": 20},
    "bag": {"price": 700, "qty": 5}
}

# Manually calculated total value (no loops)
total_value = (10 * 50) + (120 * 20) + (700 * 5)

low_stock = {
    "bag": {"price": 700, "qty": 5}   # manually decided threshold < 10
}

print(inventory)
print("Total Value:", total_value)
print("Low Stock:", low_stock)
