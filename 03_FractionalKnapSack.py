class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda item: item.value / item.weight, reverse=True)
    total_value = 0
    selected_items = []

    for item in items:
        if capacity <= 0:
            break  # Knapsack is full
        if item.weight <= capacity:
            # Take the whole item
            total_value += item.value
            capacity -= item.weight
            selected_items.append(item)
        else:
            # Take a fraction of the item to fill the knapsack
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
            selected_items.append(Item(item.value * fraction, item.weight * fraction))  

    return total_value, selected_items

# Example usage:
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
max_value, selected_items = fractional_knapsack(items, capacity)

print("Maximum value:", max_value)
print("Selected items:")
for item in selected_items:
    print(f"Value: {item.value}, Weight: {item.weight}")
