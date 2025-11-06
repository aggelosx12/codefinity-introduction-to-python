grocery_inventory  = {
"Milk": (113, "Dairy"),
"Eggs": (116, "Dairy"),
"Bread": (117, "Bakery"),
"Apples": (141, "Produce")
}
print("Details of Bread:", grocery_inventory.get("Bread"))

grocery_inventory["Cookies"] = (143 , "Bakery")
print("Updated Inventory:", grocery_inventory)

removed_item = grocery_inventory.pop("Eggs")
print("Removed Item:", removed_item)
print("Current Inventory:", grocery_inventory)