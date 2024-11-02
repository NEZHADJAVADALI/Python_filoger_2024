class Product:
    def __init__(self, id, name, price, brand):
        self.id = id
        self.name = name
        self.price = price
        self.brand = brand
    
    def display(self):
        print(f"id: {self.id} | name: {self.name} | price: {self.price} | brand: {self.brand}")
        
    
class Phone(Product):
    def __init__ (self, id, name, price, brand):
        super().__init__(id, name, price , brand)
        
class Laptop(Product):
    def __init__(self, id, name, price, brand, memory, processor):
        super().__init__(id, name, price, brand)
        self.memory = memory
        self.processor = processor
        
    def display(self):
        super().display()
        print(f"memory: {self.memory} | processor: {self.processor}")
        
class Store:
    def __init__(self):
        self.phones = []
        self.laptops = []
        
    def add(self, product):
        if isinstance(product, Phone):
            self.phones.append(product)
        elif isinstance(product, Laptop):
            self.laptops.append(product)
        else:    
            print("Product type not found!")
            
    def remove(self, id):
        for collection in (self.phones,self.laptops):
            for product in collection:
                if product.id == id:
                    collection.remove(product)
                    print(f"product with ID {id} has been removed")
                    return
        print(f"product with ID {id} not found")

    def display(self, product_type):
        if product_type == "phone":
            print(f"Phone: ")
            for phone in self.phones:
                phone.display()    
        elif product_type == "laptop":
            print("Laptop: ")
            for laptop in self.laptops:
                laptop.display()
        else: 
            print("Invalid product type.")
            
            

        
           
