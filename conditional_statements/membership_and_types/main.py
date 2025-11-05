# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99" 
count = 120

# Step 1: Membership check for the substrings "raw" and "Imported"
contains_raw = "raw" in description
contains_Imported = "Imported" in description

# Step 2: Insert the `contains_raw` and `contains_Imported` variables into the appropriate print statements
print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)

# Step 3: Use the `type()` function to check data types of the price and count variables
price_is_float = type(price) == float
count_is_int = type(count) == int

# Step 4: Insert the `price_is_float` and `count_is_int` variables into the appropriate print statements
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)