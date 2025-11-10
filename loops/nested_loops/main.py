produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]

# 3. nested loops
for section in groceries:
    for item in section:
        print(item)