# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from lines import get_lines

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.sorties_valides = set()
        self.all_characters = {}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale et l'altitude (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        nothing = Command('', "'' : la commande vide ne fait rien", Actions.nothing, 0)
        self.commands[""] = nothing
        history = Command("history", " : afficher le chemin parcouru depuis le début du jeu", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : retourner au lieu précédent, si cela est possible", Actions.back, 0)
        self.commands["back"] = back
        inventory = Command("inventory", " : regarder le contenu de son inventaire", Actions.inventory, 0)
        self.commands["inventory"] = inventory
        look = Command("look", " : chercher des objets et des personnes dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : prendre un objet dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : lâcher un objet de son inventaire", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : jeter un oeil à son inventaire", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk <character>", " : Parler au personnage", Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms

        rue = Room("Rue principale", "Je suis dans une véritable rue de western avec ses chevaux, ses cowboys et ses douilles au sol.")
        self.rooms.append(rue)
        saloon = Room("Saloon", "Ce bon vieux saloon ne m'est plus accessible car le gérant m'a viré.")
        self.rooms.append(saloon)
        sherif = Room("Bureau du shérif", "Le shérif est toujours là, histoire de veiller sur cette charmante petite ville.")
        self.rooms.append(sherif)
        chapelle = Room("Chapelle", "La chappelle est calme, je vois un hôtel au fond et un confessionnal à ma gauche.")
        self.rooms.append(chapelle)
        hotel = Room("Hotel", "Je suis dans l'entrée de l'hôtel, un réceptionniste me fait face derrière le comptoir et je vois un escalier au fond.")
        self.rooms.append(hotel)
        etage = Room("Étage", "Dans ce couloir mal éclairé, il y a 3 chambres, et de multiples objets au sol.")
        self.rooms.append(etage)
        chambre1 = Room("Chambre 1", "Une chambre tout à fait banal, avec une petite fenêtre donnant sur la rue principale")
        self.rooms.append(chambre1)
        chambre2 = Room("Chambre 2", "Cette chambre vient vraisemblablement d'être quittée en vitesse, il reste encore de nombreux objets un peu partout.")
        self.rooms.append(chambre2)
        chambre3 = Room("Chambre 3", "Ça ne ressemble plus vraiment à une chambre, mais plutôt un débarras tellement il y a de choses ici.")
        self.rooms.append(chambre3)
        zany = Room("Zany", "Cette lune me semble assez austère, elle ressemble un peu au désert que je connais bien.")
        self.rooms.append(zany)
        litchie = Room("Litchie", "Je suis entouré de végétation largement plus grande que moi, au point que je ne vois déjà presque plus mon vaisseau après quelques mètres. Mais il y a des traces de vie autour de moi.")
        self.rooms.append(litchie)
        kapry = Room("Kapry", "Ici la fête est partout et les kapryens sont déchaînés, je ne sais pas si je vais rester longtemps. À moins qu'il n'y ait un petit marché pas loin !")
        self.rooms.append(kapry)
        pandora = Room("Pandora", "Cette planète peuplée d'humanoide me terrifie, elle est surprenante de par ses constructions originales et son ciel obscur. ")
        self.rooms.append(pandora)
        jafar = Room("Jafar", 'Cette planète a un paysage plutôt désertique avec de vastes étendue de dunes de sables, on peut apercevoir une grande ville luxueuse appelée "Casino Land"')
        self.rooms.append(jafar)
        minto = Room("Minto", "Ici prospère un calme absolu, le seul bruit que j'entend est celui des vagues qui s'échoue sur cette petite île paradisiaque entourée d'eau, tout comme le reste de la planète ")
        self.rooms.append(minto)
        pollux = Room("Pollux", "Une lune des plus déconcertante chacun de mes pas est un supplice dû aux poils longs et marrons se trouvant sur le sol, ces poils proviennent des nuages")
        self.rooms.append(pollux)
        sid = Room("Sid", "Le paysage de cette lune est celui de vastes plaines vertes et de plantes, néanmoins l'air de l'atmosphère insufflé après chaque respiration me donne envie de dormir, mais je dois lutter pour rejoindre le fameux temple sacré des dormeurs.")
        self.rooms.append(sid)
        tancoeur = Room("Tancoeur","Cette planète semble refusé ma présence, moi qui suit allergique à la désolation, celle-ci est composé de pierres sombres, de montagnes noires et de volcans en activités.")
        self.rooms.append(tancoeur)

        # Create exits for rooms

        rue.exits = {"N" : saloon, "E" : hotel, "S" : chapelle, "O" : sherif, "U" : None, "D" : None}
        saloon.exits = {"N" : None, "E" : None, "S" : rue, "O" : None, "U" : None, "D" : None}
        sherif.exits = {"N" : None, "E" : rue, "S" : None, "O" : None, "U" : None, "D" : None}
        chapelle.exits = {"N" : rue, "E" : None, "S" : kapry, "O" : None, "U" : None, "D" : None}
        hotel.exits = {"N" : None, "E" : None, "S" : None, "O" : rue, "U" : etage, "D" : None}
        etage.exits = {"N" : chambre1, "E" : chambre2, "S" : None, "O" : chambre3, "U" : None, "D" : hotel}
        chambre1.exits = {"N" : None, "E" : None, "S" : etage, "O" : None, "U" : None, "D" : None}
        chambre2.exits = {"N" : None, "E" : None, "S" : None, "O" : etage, "U" : None, "D" : None}
        chambre3.exits = {"N" : etage, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        zany.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : minto}
        litchie.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : minto}
        minto.exits = {"N" : None, "E" : kapry, "S" : None, "O" : jafar, "U" : zany, "D" : litchie}
        kapry.exits = {"N" : None, "E" : pandora, "S" : None, "O" : minto, "U" : None, "D" : None}
        jafar.exits = {"N" : None, "E" : None, "S" : minto, "O" : None, "U" : pollux, "D" : sid}
        tancoeur.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : pandora}
        sid.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : jafar}
        pollux.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : jafar}
        pandora.exits = {"N" : None, "E" : None, "S" : None, "O" : kapry, "U" : tancoeur, "D" : None}
        
        # Setup sets for room's exits

        for e in self.rooms :
            self.sorties_valides = self.sorties_valides | set(e.exits.keys())

        # Setup items for rooms

        EPEE = Item("épée", "une épée au fil tranchant comme un rasoir", 2)
        rue.inventory["EPEE"] = EPEE

        # Setup PNJs for rooms 

    
        # Le dernier paramètre est pour savoir si le personnage peut changer de pièce ( 0 -> immobile)
        GANDALF = Character("Gandalf", "un magicien blanc", rue, ["Abracadabra !", "Bizzzzz"], 1)
        rue.characters["GANDALF"] = GANDALF
        PATATE = Character("Patate", "une magnifique patate", rue, [], 0)
        rue.characters["PATATE"] = PATATE
        BOB = Character("Bob", "simplement une éponge", sherif, ["Patriiiiiick"], 1)
        sherif.characters["BOB"] = BOB
        RECEPTIONNISTE = Character("Réceptionniste", 'un petit gars banal', hotel, ["Je n'ai malheureusement pas de chambres disponibles"], 0)
        hotel.characters["RECEPTIONNISTE"] = RECEPTIONNISTE

        # Setup the dict of all characters

        for r in self.rooms :
            for char in r.characters :
                self.all_characters[char] = r.characters[char]
    

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        Player.name = self.player
        #exits = [value.name for value in list(rue.exits.values()) if value != None] # test
        #print(exits) # test
        #a = list(rue.exits.values()) # test
        #print(a, a[1].name, type(a[1])) # test
        self.player.current_room = hotel
        self.player.inventory = {}
        self.player.character = {}

    # Beginning of history

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        print(f"\n\n{self.player.name} posons le contexte :\n")
        get_lines('prologue', 0)
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
