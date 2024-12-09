import player

# Define the Room class.

class Room:
    """
    La classe Room donne des méthodes pour la pièce dans lequel le joueur et une description de celle-ci.

    une description plus détaillée de la classe (optionnel) ;

    Les attributs de la classe sont :
        name : nom de la pièce
        description : une description de la pièce
        exits : les différentes sorties de la pièce
        inventory : 

    Les méthodes de la classe sont :
        __init__() : constructeur
        get_exit() : donne les sorties possibles en fonction de la direction donnée
        get_exit_string() : donne une description de la pièce vers laquelle amène la sortie
        get_long_description() : donne une description précise de la pièce actuelle ainsi que les sorties

    Les exceptions levées par la classe sont :
        None

    Doctests :
    >>> cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
    >>> cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
    >>> swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
    >>> castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
    >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
    >>> forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None}
    >>> tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : None}
    >>> forest.name
    'Forest'
    >>> tower.name
    'Tower'
    >>> forest.description
    'dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.'
    >>> tower.description
    "dans une immense tour en pierre qui s'élève au dessus des nuages."
    >>> forest.get_exit("N") == cave
    True
    >>> tower.get_exit("E")
    
    >>> forest.get_exit_string()
    'Sorties: N, S'
    """
    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = ()
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\n{self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Retourne une chaîne de caractères représentant le contenu de l'inventaire de la pièce.
        """
        if not self.inventory:
            print("Il n'y a rien ici.")
            return None
        
        result = ["La pièce contient:\n"]
        for item_name, details in self.inventory.items():
            description = details['description']
            weight = details['weight']
            quantity = details['quantity']
            result.append(f"    - {item_name} : {description} ({weight} kg) x{quantity}")
        
        return "\n".join(result)
