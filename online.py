# online shopping product class
class Product:
    def __init__(self, product_name, price,quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    # a method to display product information
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in stock: {self.quantity_in_stock}")

# ShoppingCart class
class ShoppingCart:
    # Class variable to get total carts created
    total_carts = 0

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1

    # a method to add products to the cart
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Add {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Not enough stock for {product.product_name}. Only {product.quantity_in_stock} left.")

    # A method of removing a product from the cart
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"Remove {product.product_name} from the cart.")
                return
        print(f"{product.product_name} is not in the cart.")

    # a method to display items in the cart
    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"{product.product_name} - Quantity: {quantity}")

    # a method to calculate total price of items in the cart
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

# the product objects
product1 = Product("Laptop", 1200, 5)
product2 = Product("Earphone", 800, 10)
product3 = Product("Headphones", 150, 20)

#  first shopping cart
cart1 = ShoppingCart()
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product3, 2)
cart1.display_cart()
print(f"Total for Cart 1: ${cart1.calculate_total()}\n")

# second shopping cart
cart2 = ShoppingCart()
cart2.add_to_cart(product2, 1)
cart2.add_to_cart(product3, 3)
cart2.remove_from_cart(product3)  # Remove one product
cart2.display_cart()
print(f"Total for Cart 2: ${cart2.calculate_total()}")
