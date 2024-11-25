# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        nothing = Command('', "'' : la commande vide ne fait rien", Actions.nothing, 0)
        self.commands[""] = nothing
        # Setup rooms

        rue = Room("Rue principale", "Une véritable rue de western avec ses chevaux, ses cowboys et ses douilles au sol.")
        self.rooms.append(rue)
        saloon = Room("Saloon", "Ce bon vieux saloon ne vous est plus accessible car le gérant vous a viré.")
        self.rooms.append(saloon)
        sherif = Room("Bureau du shérif", "Le shérif est toujours là, histoire de veiller sur cette charmante petite ville.")
        self.rooms.append(sherif)
        chapelle = Room("Chapelle", "La chappelle est calme, vous y trouvez un hôtel au fond et un confessionnal à votre gauche.")
        self.rooms.append(chapelle)
        hotel = Room("Hotel", "Vous vous situez dans l'entrée de l'hôtel, un réceptionniste vous fait face derrière le comptoir et vous voyez un escalier au fond.")
        self.rooms.append(hotel)
        etage = Room("Étage", "Dans ce couloir mal éclairé, vous distinguez 3 chambres autour de vous, et de multiples objets au sol.")
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
        kapry = Room("Kapry", "Ici la fête est partout et les kapryens sont déchaînés, je ne sais pas si je vais rester longtemps. À moins que, il y a un petit marché pas loin !")
        self.rooms.append(kapry)
        pandora = Room("Pandora", "")
        self.rooms.append(pandora)
        jafar = Room("Jafar", "")
        self.rooms.append(jafar)
        minto = Room("Minto", "")
        self.rooms.append(minto)
        pollux = Room("Pollux", "")
        self.rooms.append(pollux)
        sid = Room("Sid", "")
        self.rooms.append(sid)
        tancoeur = Room("Tancoeur","")
        self.rooms.append(tancoeur)

        # Create exits for rooms

        saloon.exits = {"N" : None, "E" : rue, "S" : None, "O" : None}
        sherif.exits = {"N" : None, "E" : rue, "S" : None, "O" : None}
        chapelle.exits = {"N" : None, "E" : rue, "S" : kapry, "O" : None}
        hotel.exits = {"N" : None, "E" : etage, "S" : None, "O" : rue}
        etage.exits = {"N" : chambre1, "E" : chambre2, "S" : None, "O" : chambre3}
        chambre1.exits = {"N" : None, "E" : None, "S" : etage, "O" : None}
        chambre2.exits = {"N" : None, "E" : None, "S" : None, "O" : etage}
        chambre3.exits = {"N" : etage, "E" : None, "S" : None, "O" : None}
        zany.exits = {"N" : None, "E" : None, "S" : minto, "O" : None}
        litchie.exits = {"N" : minto, "E" : None, "S" : None, "O" : None}
        minto.exits = {"N" : zany, "E" : kapry, "S" : litchie, "O" : jafar}
        kapry.exits = {"N" : None, "E" : pandora, "S" : None, "O" : minto}
        jafar.exits = {"N" : pollux, "E" : sid, "S" : minto, "O" : None}
        tancoeur.exits = {"N" : None, "E" : None, "S" : pandora, "O" : None} 
        sid.exits = {"N" : None, "E" : None, "S" : None, "O" : jafar}
        pollux.exits = {"N" : None, "E" : None, "S" : jafar, "O" : None}
        pandora.exits = {"N" : tancoeur, "E" : None, "S" : None, "O" : kapry}
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = rue

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
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()


if __name__ == "__main__":
    main()
