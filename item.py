class Item:
    
    def __init__(self, name, description, quantity, drop_or_not = 1) :
        '''drop_or_not : 1 si on peut le jeter de son inventaire'''
        self.name = name
        self.description =  description
        self.quantity = quantity
        self.drop_or_not = drop_or_not
    
#------------------------------------

    def __str__(self):
        return f"{self.quantity}x {self.name} : {self.description}"
