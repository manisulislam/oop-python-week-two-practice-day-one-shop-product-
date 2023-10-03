""" 
Sunscreen for body
Cleanser
Toner
Moisturizer with SPF/antioxidants for daytime
Moisturizer with retinol for nighttime
Eye cream
Lip balm
Light hand lotion
Blemish gel
Shower gel
Antiperspirant
Cologne

"""

class Product:
    def __init__(self, name, id, price,size, quantity ):
        self.name=name
        self.id=id
        self.price=price
        self.size=size
        self.quantity=quantity


class Shop:

    # initialization
    def __init__(self, name):
        self.store=[]
       
    
    # add to product
    def add_to_product(self, product ):
        if isinstance(product, Product):
            self.store.append(product)
            print(f"{product.name} added successfully..")
        else:
            print(f"invalid product..")
    
    # buy_product
    def buy_product(self, product_name):
        
        for item in self.store:
            if item.name==product_name and item.quantity>0:
                congrats=f"congratualations..{item.product_name} has found"
                print(congrats)
            else:
                res=f"{item.name} not found"
                print(res)



    
productOne= Product("sunscreen",1001,250,20,30)
productTwo =Product("eyecream",1002,300,500,20)
productThree=Product("showergel",1003,600,120,25)

Shop.add_to_product(productOne)
Shop.add_to_product(productTwo)
Shop.add_to_product(productThree)

Shop.buy_product("sunscreen")


