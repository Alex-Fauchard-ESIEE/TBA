"""La classe Player permet au joueur d'intéragir avec les éléments
et l'histoire."""
class Player():
    """
    Cette classe permet au joeur d'intéragir avec les éléments
    et l'histoire.

    une description plus détaillée de la classe ;

    Les attributs de la classe sont :
        name : nom du joueur
        history : liste des pièces où le joueur a été
        current_room : pièce actuelle du joueur
        inventory : objets contenus dans l'inventaire du joueur

    Les méthodes de la classe sont : 
        __init__() : constructeur
        get_name() : donne le nom du joueur
        move() : permet au joueur de se déplacer
        get_inventory() : donne les objets contenu dans l'inventaire du joueur

    Les exceptions levées par la classe sont :
        None
    
    Doctests :
    >>> Patrick = Player('Patrick')
    >>> from room import Room
    >>> swamp = Room("Swamp", "dans un marécage sombre et ténébreux.")
    >>> forest = Room("Forest", "Vous entendez une brise légère à travers la cime des arbres.")
    >>> castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis.")
    >>> Patrick.name
    'Patrick'
    >>> Patrick.current_room = castle
    >>> castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}
    >>> Patrick.move("N")
    Vous êtes dans un énorme château fort avec des douves et un pont levis.
    
    Sorties: N, E

    """

#------------------------------------

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
        self.inventory = {}

#------------------------------------

    def get_name(self):
        '''

        Objectif :
        Donne le nom du joueur.

        Arguments :
        self

        '''
        return 'self.name'
#------------------------------------

    def get_history(self):
        '''

        Objectif :
        Donner la liste des pièce par lesquelles le joueur est passé.

        Arguments :
        self

        '''
        history = "\nVous avez déjà visité les pièces suivantes :\n"
        if not self.history :
            return ''
        for room in self.history :
            history += "- " + str(room.name) + "\n"
        return history

#------------------------------------

    def move(self, direction):
        '''

        Objectif :
        Permet au joueur de se déplacer.

        Arguments :
        self
        direction (str)

        '''
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        print(self.get_history())
        return True

#------------------------------------

    def get_inventory(self):
        '''

        Objectif :
        Donner l'inventaire du joueur.

        Arguments :
        self

        '''
        if not self.inventory :
            print("\nVotre inventaire est vide.")
            return ''

        result = "\nVous disposez des items suivants :\n"
        for item in self.inventory.values():
            result += f"    - {item.quantity}x {item.name} : {item.description}\n"
        return result
