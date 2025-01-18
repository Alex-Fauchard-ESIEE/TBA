"La classe Item permet d'intéragir et de spécifier des paramètres aux objets."

# La classe Item est légitime dans son existence, mais pylint la trouve trop petite,
# on désactive donc exceptionnellement le contrôle
# pylint: disable=too-few-public-methods
class Item:
    """
    La classe Room donne des méthodes pour la pièce dans lequel
    le joueur et une description de celle-ci.

    une description plus détaillée de la classe ;

    Les attributs de la classe sont :
        name : nom de l'objet
        description : une description de l'objet
        qunaitity : quanitité de l'objet
        drop_or_not : permet de savoir si on peut jeter l'objet de notre inventaire

    Les méthodes de la classe sont : 
        __init__() : constructeur
        __str__() : permet de redéfinir le print()

    Les exceptions levées par la classe sont :
        None
    """

#------------------------------------

    def __init__(self, name, description, quantity, drop_or_not = 1) :
        self.name = name
        self.description =  description
        self.quantity = quantity
        self.drop_or_not = drop_or_not

#------------------------------------

    def __str__(self):
        return f"{self.quantity}x {self.name} : {self.description}"
