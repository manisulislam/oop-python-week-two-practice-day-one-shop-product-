class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"{product.name} has been added to the shop.")
        else:
            print("Invalid product. Please provide a valid Product object.")

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name and product.quantity > 0:
                product.quantity -= 1
                print(f"Congratulations! You have successfully purchased {product.name}.")
                return
        print(f"Sorry, {product_name} is not available in the shop or it is out of stock.")

# Example usage:
if __name__ == "__main__":
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Smartphone", 500, 10)

    shop = Shop()
    shop.add_product(product1)
    shop.add_product(product2)

    shop.buy_product("Laptop")
    shop.buy_product("Smartphone")
    shop.buy_product("Tablet")
