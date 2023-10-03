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
    def __init__(self):
        self.store=[]
       
    
    # add to product
    def add_to_product(self, product ):
        if isinstance(product, Product):
            self.store.append(product)
            print(f"{product.name} added successfully..")
        else:
            print(f"invalid product..")
    
    # buy_product
    def buy_product(self, pro_name):
        
        for item in self.store:
            if item.name==pro_name and item.quantity>0:
                congrats=f"congratualations..{item.name} has found"
                print(congrats)
                break
            else:
                res=f"{pro_name} not found"
                print(res)



s= Shop()
productOne= Product("sunscreen",1001,250,20,30)
productTwo =Product("eyecream",1002,300,500,20)
productThree=Product("showergel",1003,600,120,25)

s.add_to_product(productOne)
s.add_to_product(productTwo)
s.add_to_product(productThree)

s.buy_product("sunscreen")


