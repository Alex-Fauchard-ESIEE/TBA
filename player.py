# Define the Player class.
class Player():
    """
    Cette classe permet au joeur de bouger et de révéler sa position

    attribut 1 : self.name
    attribut 2 : self.current_name
    attribut 3 : self.inventory

    __init__ : définie le constructeur
    move () : donne le procéder pour changer de room


    une liste des exceptions levées par la classe (optionnel) ;

    Doctests :
    >>> Patrick = Player('Patrick')
    >>> from room import Room
    >>> swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
    >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
    >>> Patrick.name
    'Patrick'
    >>> Patrick.current_room = castle
    >>> castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}
    >>> Patrick.move("N")
    Vous êtes dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.
    
    Sorties: N, E

    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
        self.inventory = {}
      
#------------------------------------
    #Define get_name
    def get_name(self):
        return f'self.name'
#------------------------------------
    # Define get_history
    def get_history(self):
        history = "\nVous avez déjà visité les pièces suivantes:\n"
        if self.history == [] :
            return ''
        else :
            for room in self.history :
                history += "- " + str(room.name) + "\n"
        return history
            
#------------------------------------

    # Define the move method.
    def move(self, direction):
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
        """
        Retourne une chaîne de caractères représentant le contenu de l'inventaire du joueur.
        """
        if self.inventory == {} :
            print("\nVotre inventaire est vide.")
            return ''
        
        result = "\nVous disposez des items suivants :\n"
        for item in self.inventory.values():
            result += f"    - {item.name} : {item.description} ({item.weight} kg)\n"
        return result
        
