import sys

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def __str__(self):
        return f"Code: {self.code}, Name: {self.name}, Price: ${self.price:.2f}"

class ShopInventory:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        if code in self.products:
            print(f"Error: Product with code '{code}' already exists.")
        else:
            self.products[code] = Product(code, name, price)
            print(f"Product '{name}' added successfully.")

    def display_products(self):
        if not self.products:
            print("No products available in the inventory.")
        else:
            print("\n--- Inventory ---")
            for product in self.products.values():
                print(product)
            print("-----------------\n")

    def remove_product(self, code):
        if code in self.products:
            removed_product = self.products.pop(code)
            print(f"Product '{removed_product.name}' removed successfully.")
        else:
            print(f"Error: Product with code '{code}' not found.")

    def edit_product(self, code):
        product = self.products.get(code)
        if product:
            new_name = input(f"Enter new name (current: {product.name}) or press Enter to keep unchanged: ").strip()
            new_price = input(f"Enter new price (current: {product.price}) or press Enter to keep unchanged: ").strip()

            if new_name:
                product.name = new_name
            if new_price:
                try:
                    product.price = float(new_price)
                    if product.price < 0:
                        raise ValueError("Price cannot be negative.")
                except ValueError:
                    print("Invalid price. Price unchanged.")
            
            print(f"Product '{code}' updated successfully.")
        else:
            print(f"Error: Product with code '{code}' not found.")

    def search_product(self, search_term):
        results = [product for product in self.products.values()
                   if product.code == search_term or product.name.lower() == search_term.lower()]
        if results:
            print("\n--- Search Results ---")
            for product in results:
                print(product)
            print("----------------------\n")
        else:
            print(f"No products found matching '{search_term}'.")

    def display_inventory_summary(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            total_value = sum(product.price for product in self.products.values())
            print(f"Total number of products: {len(self.products)}")
            print(f"Total value of inventory: ${total_value:.2f}")

    def show_help(self):
        print("""
Available Commands:
1. add     - Add a new product (requires code, name, and price).
2. display - Display all products.
3. remove  - Remove a product by its unique code.
4. edit    - Edit an existing product by code.
5. search  - Search for a product by code or name.
6. summary - Display inventory summary (total number of products and total value).
7. help    - Show this help message.
8. exit    - Exit the program.
        """)

def get_valid_price():
    while True:
        try:
            price = float(input("Enter product price: ").strip())
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except ValueError as e:
            print(f"Invalid input: {e}")

def main():
    shop = ShopInventory()

    print("Welcome to the Shop Inventory Manager!")
    shop.show_help()

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == 'add':
            code = input("Enter product code: ").strip()
            name = input("Enter product name: ").strip()
            price = get_valid_price()
            shop.add_product(code, name, price)

        elif command == 'display':
            shop.display_products()

        elif command == 'remove':
            code = input("Enter product code to remove: ").strip()
            shop.remove_product(code)

        elif command == 'edit':
            code = input("Enter product code to edit: ").strip()
            shop.edit_product(code)

        elif command == 'search':
            search_term = input("Enter product code or name to search: ").strip()
            shop.search_product(search_term)

        elif command == 'summary':
            shop.display_inventory_summary()

        elif command == 'help':
            shop.show_help()

        elif command == 'exit':
            print("Exiting program. Goodbye!")
            sys.exit()

        else:
            print("Invalid command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    main()

