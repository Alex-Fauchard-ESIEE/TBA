"""La classe Room donne des méthodes pour la pièce dans lequel
le joueur et une description de celle-ci."""

class Room:
    """
    La classe Room donne des méthodes pour la pièce dans lequel
    le joueur et une description de celle-ci.

    une description plus détaillée de la classe ;

    Les attributs de la classe sont :
        name : nom de la pièce
        description : une description de la pièce
        exits : les différentes sorties de la pièce
        inventory : objets contenus dans la pièce
        characters : personnages dans la pièce
        zone : zone de la map à laquelle la pièce appartient (1 ou 2)
        talk : permet de savoir si une pièce à un dialogue

    Les méthodes de la classe sont : 
        __init__() : constructeur
        get_exit() : donne les sorties possibles en fonction de la direction donnée
        get_exit_string() : donne une description de la pièce vers laquelle amène la sortie
        get_long_description() : donne une description de la pièce actuelle avec ses sorties
        get_inventory() : donne les objets et les personnages de la pièce

    Les exceptions levées par la classe sont :
        None

    Doctests :
    >>> cave = Room("Cave", "dans une grotte profonde et sombre.")
    >>> cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume.")
    >>> swamp = Room("Swamp", "dans un marécage sombre et ténébreux.")
    >>> castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis.")
    >>> forest = Room("Forest", "Vous entendez une brise légère à travers la cime des arbres.")
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

#------------------------------------

    # Define the constructor.
    def __init__(self, name, description, zone,talk = 0):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}
        self.zone = zone
        self.talk = talk

#------------------------------------

    # Define the get_exit method.
    def get_exit(self, direction):
        '''

        Objectif :
        Permet d'obtenir la pièce de sortie dans la direction donnée.

        Arguments :
        self
        direction (str)

        '''
        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        return None

#------------------------------------

    # Return a string describing the room's exits.
    def get_exit_string(self):
        '''

        Objectif :
        Permet d'afficher les sorties d'une pièce.


        Argument :
        self

        '''
        pluriel = 0
        exit_string = ""
        for sortie in self.exits:
            if self.exits.get(sortie) is not None:
                pluriel += 1
                exit_string += sortie + " (" + self.exits.get(sortie).name + ")" + ", "
        if pluriel >= 2 :
            exit_string = "Sorties : " + exit_string
        else :
            exit_string = "Sortie : " + exit_string
        exit_string = exit_string.strip(", ")
        return exit_string

#------------------------------------

    # Return a long description of this room including exits.
    def get_long_description(self):
        '''

        Objectif :
        Permet d'obtenir la description précise d'une pièce.

        Argument :
        self

        '''
        return f"""\n{self.description}

Position actuelle : {self.name}

{self.get_exit_string()}\n"""

#------------------------------------

    def get_inventory(self):
        '''

        Objectif :
        Permet d'obtenir l'inventaire d'une pièce (objets et personnages).

        Argument :
        self

            '''
        if not self.inventory and not self.characters  :
            print("\nIl n'y a rien d'intéressant ici...")
            return ''

        result = "\nOn voit :\n"
        for item in self.inventory.values():
            result += f"    - {item.quantity}x {item.name} : {item.description}\n"
        for character in self.characters.values() :
            result += f"    - {character.name} : {character.description}\n"
        return result
