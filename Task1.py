#This Task represents a custom PC builder program, which allows users to choose components for their computers (PC's) and calculates the total price including any additional items and discounts.
# Arrays to store item information
item_codes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
item_descriptions = [
    "Compact Case", "Tower Case", "8 GB RAM", "16 GB RAM", "32 GB RAM",
    "1 TB HDD", "2 TB HDD", "4 TB HDD",
    "240 GB SSD", "480 GB SSD",
    "1 TB Second HDD", "2 TB Second HDD", "4 TB Second HDD",
    "DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer",
    "Standard OS", "Professional OS"
]
item_prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Function to display available items
def display_items():
    print("Available Items:")
    for i in range(len(item_codes)):
        print(f"{item_codes[i]}\t{item_descriptions[i]}\t${item_prices[i]:.2f}")

# Function to choose an item from a category
def choose_item(category_name, category_items):
    print(f"\nChoose a {category_name}:")
    display_items()
    while True:
        chosen_item = input(f"Enter the item code for your {category_name} choice (or 'done' to finish): ").upper()
        if chosen_item in category_items:
            return chosen_item
        elif chosen_item.lower() == 'done':
            return None
        else:
            print("Invalid item code. Please try again.")

# Main program
print("Welcome to the Custom PC Builder!")
print("You can choose one case, one RAM, and one Main Hard Disk Drive for your computer.")

# Choose components for PC
chosen_case = choose_item("Case", ["A1", "A2"])
chosen_ram = choose_item("RAM", ["B1", "B2", "B3"])
chosen_hdd = choose_item("Main Hard Disk Drive", ["C1", "C2", "C3"])

# Calculates the total price of basic components
basic_components_price = 200.00

# Calculate the price of chosen items
chosen_items_price = sum(item_prices[item_codes.index(item)] for item in [chosen_case, chosen_ram, chosen_hdd])

# Calculate the total price including the chosen items
total_price = basic_components_price + chosen_items_price

# List to store additional items
additional_items = []

# Allow the customers to choose additional items
while True:
    print("\nChoose additional items from any category:")
    additional_item = choose_item("Additional Item", item_codes)
    if additional_item:
        additional_items.append(additional_item)
    else:
        break

# To Calculate the price of additional items
additional_items_price = sum(item_prices[item_codes.index(item)] for item in additional_items)

# To Update the total price with the additional items
total_price += additional_items_price

# To Determine the discount based on the number of additional items
if len(additional_items) == 1:
    discount = 0.05  # 5% discount for one additional item
elif len(additional_items) >= 2:
    discount = 0.10  # 10% discount for two or more additional items
else:
    discount = 0  # No discount

# To Calculate the discount amount
discount_amount = discount * total_price

# To Apply the discount to the total price
total_price -= discount_amount

# To Display chosen items, additional items, discount, amount saved, and the new total price
print("\nChosen Components:")
print(f"Case: {chosen_case} - {item_descriptions[item_codes.index(chosen_case)]}")
print(f"RAM: {chosen_ram} - {item_descriptions[item_codes.index(chosen_ram)]}")
print(f"Main Hard Disk Drive: {chosen_hdd} - {item_descriptions[item_codes.index(chosen_hdd)]}")

if additional_items:
    print("\nChosen Additional Items:")
    for item in additional_items:
        print(f"{item} - {item_descriptions[item_codes.index(item)]}")

print(f"Total Price (before discount): ${total_price + discount_amount:.2f}")
print(f"Discount Applied: {discount * 100}%")
print(f"Amount Saved: ${discount_amount:.2f}")
print(f"New Total Price (after discount): ${total_price:.2f}")
