class Item:
    
    def __init__(self, name, description, quantity):
        self.name = name
        self.description =  description
        self.quantity = quantity
    
#------------------------------------

    def __str__(self):
        return f"{self.quantity}x {self.name} : {self.description}"
