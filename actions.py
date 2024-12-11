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
# 
MSG2 = "\nLa direction '{direction}' n'existe pas.\n"

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
            #print(direction) c'etait un test
        if direction in game.sorties_valides :
            #print(game.sorties_valides) c'etait un test
            player.move(direction)
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
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

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
        obj = list_of_words[1].capitalize
        if list_of_words[1] in player.current_room.inventory :
            del player.current_room.inventory[list_of_words[1]]
            player.inventory[list_of_words[1]] = f"    - {list_of_words[1].name} : {list_of_words[1].description} ({list_of_words[1].weight} kg)\n"
            print(obj,"est maintenant bien au chaud dans ton inventaire.")
            return player.inventory
        else :
            print(obj ," n'est pas dans la pièce.")
        return None

#------------------------------------

    def drop(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        obj = list_of_words[1].capitalize
        if list_of_words[1] in player.inventory :
            player.inventory.remove(list_of_words[1])
            player.current_room.inventory.add(list_of_words[1])
            print(obj,"est maintenant sur le sol froid.")
            return game.current_room.inventory
        else :
            print(obj ," n'est pas dans ton inventaire.")
        return None

#------------------------------------

    def check(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print(game.player.inventory)
        return None