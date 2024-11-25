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

        rue = Room("Rue principale", "")
        self.rooms.append(rue)
        saloon = Room("Saloon", "")
        self.rooms.append(saloon)
        sherif = Room("Bureau du shérif", "")
        self.rooms.append(sherif)
        chapelle = Room("Chapelle", "")
        self.rooms.append(chapelle)
        hotel = Room("Hotel","")
        self.rooms.append(hotel)
        etage = Room("Étage", "")
        self.rooms.append(etage)
        chambre1 = Room("Chambre 1", "")
        self.rooms.append(chambre1)
        chambre2 = Room("Chambre 2", "")
        self.rooms.append(chambre2)
        chambre3 = Room("Chambre 3", "")
        self.rooms.append(chambre3)
        zany = Room("Zany", "")
        self.rooms.append(zany)
        litchie = Room("Litchie", "")
        self.rooms.append(litchie)
        kapry = Room("Kapry", "sur une planète riche en sucrerie et en fantaisie de toutes. Les kapryciens sont joyeux, gentils et festifs.")
        self.rooms.append(kapry)
        pandora = Room("Pandora", "sur une planète avec des humains géants")
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
