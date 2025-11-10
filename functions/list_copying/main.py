def apply_discount(prices):
    # Create a copy of the `prices` list
    prices_copy = prices.copy()
    # Iterate through the copied list by index
    for i in range(len(prices_copy)):
        # Apply a 10% discount if the price is greater than $2.00
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.90
    # Return the updated list of prices
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# Print the updated prices
print(f"Updated product prices: {updated_prices}")