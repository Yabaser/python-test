# Defining the parent class
class Product:

    #Defining the attributes
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
    
    #Defining the parent method
    def display_details(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name : {self.name}")

#Defining the child class A
class ProductA(Product):
    def __init__(self,product_id,name,count,category):
        super().__init__(product_id, name)
        self.count = count
        self.category = category
    
    def display_details(self):
        super().display_details()
        print(f"Count for A: {self.count}")
        print(f"Category: {self.category}")

#Defining the child class B
class ProductB(Product):
    def __init__(self,product_id,name,count,category):
        super().__init__(product_id, name)
        self.count = count
        self.category = category
    
    def display_details(self):
        super().display_details()
        print(f"Count for B: {self.count}")
        print(f"Category: {self.category}")

#Defining the child class C
class ProductC(Product):
    def __init__(self,product_id,name,count,category):
        super().__init__(product_id, name)
        self.count = count
        self.category = category
    
    def display_details(self):
        super().display_details()
        print(f"Count for C: {self.count}")
        print(f"Category: {self.category}")

#Creating objects for each classes and invoking methods


P2 = ProductA(product_id = 78, name = "Amul", count=50,category="butter")

P2.display_details()

P3 = ProductB(product_id= 78, name = "Amul", count = 90, category = "Milk")

P3.display_details()

P4 = ProductC(product_id = 78, name = "Amul", count = 56, category = "choco" )

P4.display_details()
