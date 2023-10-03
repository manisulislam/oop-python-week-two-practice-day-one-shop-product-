class Hani_supar_shop:
    def __init__(self,costomer_name,age,phone_number,address) -> None:
        self.costomer_name = costomer_name
        self.age = age
        self.phone_number = phone_number
        self.address = address
    

class Product(Hani_supar_shop):

    def __init__(self, costomer_name, age, phone_number, address,item_name,price,brand,quantity) -> None:
        self.item_name = item_name
        self.price = price
        self.brand = brand
        self.quantity = quantity
        super().__init__(costomer_name, age, phone_number, address)


class shop(Product):
    def __init__(self, costomer_name, age, phone_number, address, item_name, price, brand, quantity) -> None:
        self.cart_add = [] # class in a instance 
        super().__init__(costomer_name, age, phone_number, address, item_name, price, brand, quantity)
    

    def add_to_cart(self,item,price,quantity):
        Product_equation = {'item ': item,'price' : price , 'quantity' : quantity}
        self.cart_add.append(Product_equation)
    
    def Payment(self,amount):

        Total_product_bill =  0

        for item in self.cart_add:

            Total_product_bill += item['price'] * item['quantity']
            
        print('You are total bill : ',Total_product_bill)

        
        if amount < Total_product_bill:
            print(f'Please provide {Total_product_bill - amount} more maney ')
        
        else:
            extra_maney =   amount - Total_product_bill
            print(f'Here is items and extra maney {extra_maney}')
    
    def __repr__(self) -> str:
        return f'Customer name: {self.costomer_name}, Age: {self.age}, Phone number: {self.phone_number}, Current address: {self.address}, Product name: {self.item_name}, Product price: {self.price}, Brand: {self.brand}, Product quantity: {self.quantity}'


t = int(input('<------------ YOUR PROGRAM RUNING AND PRESS 1 AND 2 PRESS PROGRAM CLOSED ------------ : '))
while t!=0:
    if (t == 1):
        csname = input('Your are name: ')
        csage = int(input('You are age :'))
        csphone = int(input('Your phone number : '))
        csaddress = input('You are current addresss : ')
        csproductName = input('Product name : ')
        csproduct_price = float(input('Product price : '))
        csbrand = input('product brand : ')
        csquantity = int(input('product quantity : '))

        costomer_info = shop(csname,csage,csphone,csaddress,csproductName,csproduct_price,csbrand,csquantity)



        print("<----------- PRODUCT NAME AND PRICE AND QUENTITY -------------->")
        costomer_info.add_to_cart(csproductName,csproduct_price,csquantity)
        print(costomer_info.cart_add)

        payment_amount =  float(input("Plase Enter Your Amount : "))
        print(costomer_info.Payment(payment_amount))
    else:
        print("program closed ")
        break
