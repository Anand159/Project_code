import json
import os

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }
    

class Inventory:
    def __init__(self, filepath):
        self.filepath = filepath
        self.products = []
        self.load_products()

    def load_products(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath, 'r') as file:
                self.products = [Product(**data) for data in json.load(file)]

    def save_products(self):
        with open(self.filepath, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=2)

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        new_product = Product(product_id, name, price, quantity)
        self.products.append(new_product)
        self.save_products()
        print(f"Product '{name}' with ID '{product_id}' added successfully.")

    def update_quantity(self):
        product_id = input("Enter product ID to update: ")
        quantity = int(input("Enter quantity to add : "))
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += quantity
                self.save_products()
                print(f"Updated quantity for '{product.name}' to {product.quantity}.")
                return
        print(f"Product ID '{product_id}' not found.")

    def sell_product(self):
        product_id = input("Enter product ID to sell: ")
        quantity = int(input("Enter quantity to sell: "))
        for product in self.products:
            if product.product_id == product_id:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    self.save_products()
                    print(f"Sold {quantity} of '{product.name}'. Remaining stock: {product.quantity}.")
                else:
                    print(f"Not enough stock for '{product.name}'. Available: {product.quantity}.")
                return
        print(f"Product ID '{product_id}' not found.")

    def check_stock(self):
        if not self.products:
            print("No products in inventory.")
            return

        low_stock_products = []
        print("------------------------------------------------")
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print("------------------------------------------------")
            if product.quantity < 10:
                low_stock_products.append(product.name)

        if low_stock_products:
            print("Warning: The following products have low stock (less than 10):")
            print(low_stock_products)

def display_menu():
    print("\n")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Update Product Quantity")
    print("4. Check Stock Levels")
    print("5. Exit")

def main():
    inventory = Inventory("inventory.json")
    
    while True:
        display_menu()
        choice = input("Please select an option: ")

        if choice == '1':
            inventory.add_product()
        elif choice == '2':
            inventory.sell_product()
        elif choice == '3':
            inventory.update_quantity()
        elif choice == '4':
            inventory.check_stock()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":
    main()


