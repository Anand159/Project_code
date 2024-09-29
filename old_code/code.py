class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


def add_product(products):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹ "))
    quantity = int(input("Enter product quantity: "))
    product = Product(product_id, name, price, quantity)
    products.append(product)
    print("Product added successfully.")

def update_quantity(products):
    product_id = input("Enter product ID to update: ")
    for product in products:
        if product.product_id == product_id:
            quantity_change = int(input("Enter quantity to add: "))
            product.quantity += quantity_change
            print(f"Updated quantity for {product.name}: {product.quantity}")
            return
    print("Product not found.")

def sell_product(products):
    product_id = input("Enter product ID to sell: ")
    quantity_sold = int(input("Enter quantity to sell: "))
    for product in products:
        if product.product_id == product_id:
            if product.quantity >= quantity_sold:
                product.quantity -= quantity_sold
                print(f"Sold {quantity_sold} of {product.name}. Remaining quantity: {product.quantity}")
                return
            else:
                print("Insufficient stock.")
                return
    print("Product not found.")

def check_stock(products):
    if not products:
        print("No products available.")
    else:
        for product in products:
            print(f"ID: {product.product_id}, Product: {product.name}, Price: ₹{product.price}, Quantity: {product.quantity}")



products = []

while True:
    print("\n---Inventory Management System---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Sell Product")
    print("4. Check Stock Levels")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        add_product(products)
        continue
    elif choice == '2':
        update_quantity(products)
    elif choice == '3':
        sell_product(products)
    elif choice == '4':
        check_stock(products)
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")



