# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    print("Final price after discount:" if discount_percent >= 20 else "No discount applied.")
    print(f"Price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")
