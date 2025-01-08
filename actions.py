from lines import get_lines
from lines import dialogues
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
# The MSG2 variable is used when the direction doesn't exist.
MSG2 = "\nLa direction '{direction}' n'existe pas.\n"
# The npc_spe dict is for npc with special speeches.
npc_spe = {'RECEPTIONNISTE' : 1}
class Actions:

#------------------------------------
# Prise en compte de la commande vide

    def nothing(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return None

#------------------------------------

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction and altitude (N, E, S, O, U, D).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        # Move the player in the direction specified by the parameter.
        direction = list_of_words[1].upper()
        if direction in {"NORD", "SUD", "OUEST", "EST", "DOWN", "UP"} :
            direction = direction[0]
        if direction in game.sorties_valides :
            player.move(direction)

            ### La seconde partie du code permet au pnjs de bouger de façon aléatoire ###
            #print(game.all_characters) #test
            for char in game.all_characters :
                ach = game.all_characters[char]
                # print(r.characters) # test
                if ach.move_or_not == 1 :
                    # print("Voilà : ", char, "et", type(char)) # test
                    temp = ach.current_room
                    ach.move()
                    if temp != ach.current_room :
                        del temp.characters[char]
                        ach.current_room.characters[char] = ach
                print(char, ":",ach.current_room.name) # test
        else :
            print(MSG2.format(direction=list_of_words[1]))
        return True
    
#------------------------------------

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci d'avoir joué {player.name}.\nÀ la prochaine !\n"
        print(msg)
        game.finished = True
        return True

#------------------------------------

    def history(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        print(player.get_history())
        return True
    
#------------------------------------

    def back(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        liste_valeurs = [e for e in player.current_room.exits.values() if e != None] # On récupère uniquement les sorties non vides.
        #print(player.history[-1], type(player.history[-1])) # test

        if player.history == [] :
            print("Tu ne peux pas revenir en arrière, tu es déjà au point de départ !\n")
        elif player.history != [] and player.history[-1] in liste_valeurs :
            player.current_room = game.player.history[-1]
            print(player.current_room.get_long_description())
            del player.history[-1]
            print(player.get_history())
        elif player.history != [] and player.history[-1] not in liste_valeurs :
            print("Tu ne peux pas revenir en arrière car le passage est à sens unique.\n")
        return None
      
#------------------------------------
  
    def inventory(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        print(player.get_inventory())
        return True

#------------------------------------

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
#------------------------------------

    def look(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        print(player.current_room.get_long_description())
        print(player.current_room.get_inventory())
            
#------------------------------------

    def take(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        obj_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        #print(obj_recherche) # test
        if obj_recherche in player.current_room.inventory :
            player.inventory[obj_recherche] = player.current_room.inventory[obj_recherche]
            print(player.inventory[obj_recherche].name.capitalize(),"est maintenant bien au chaud dans ton inventaire.")
            del player.current_room.inventory[obj_recherche]
            return player.inventory
        else :
            print(list_of_words[1].capitalize() ,"n'est pas dans la pièce.")
        return None

#------------------------------------

    def drop(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        #print(player.inventory) # test
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        obj_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        if obj_recherche in player.inventory :
            player.current_room.inventory[obj_recherche] = player.inventory[obj_recherche]
            print(player.inventory[obj_recherche].name.capitalize(),"est maintenant sur le sol froid.")
            del player.inventory[obj_recherche]
            return player.current_room.inventory
        else :
            print(list_of_words[1].capitalize() ," n'est pas dans ton inventaire.")
        return None

#------------------------------------

    def check(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(game.player.get_inventory())
        return None
    
#------------------------------------

    def talk(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        character_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        if character_recherche in npc_spe and npc_spe[character_recherche] != 0 :
            get_lines(character_recherche, len(dialogues[character_recherche])-npc_spe[character_recherche])
            npc_spe[character_recherche] -= 1
        elif character_recherche in player.current_room.characters :
            print(player.current_room.characters[character_recherche].get_msg())
            return True
        else :
            print("Hmmmm personne ici ne s'appelle comme ça")
            return False