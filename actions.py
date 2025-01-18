'''Description: The actions module :

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
'''
from lines import get_lines
from lines import dialogues

# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
# The MSG2 variable is used when the direction doesn't exist.
MSG2 = "\nLa direction '{direction}' n'existe pas.\n"
# The MSG3 variable is used especially for drop and take.
MSG3 = "\nLa commande '{command_word}' prend 1 ou 2 paramètres.\n"
# The npc_spe dict is for npc with special speeches.
npc_spe = {
'RECEPTIONNISTE' : 1, 
'SHERIF' : 2, 
'EXTRATERRESTRE' : 1, 
'GARDIEN' : 2, 
'BAKOU' : 2, 
'JARJARBINKS' : 3
}

class Actions:
    """
    La classe Actions donne des méthodes pour intéragir dans le jeu.

    une description plus détaillée de la classe ;

    Les attributs de la classe sont :
    Il n'y a pas d'attribut de classe car c'est une classe statique.

    Les méthodes statiques de la classe sont : 
        nothing() : permet au joueur de ne pas déclencher d'erreur s'il n'écrit rien
        go() : permet de déplacer le joueur et les pnjs
        quit() : permet au joueur de quitter le jeu
        history() : permet au joueur d'obtenir l'historiqe des pièces visitées
        back() : permet au joueur de revenir dans la pièce précédente
        direction () : permet au joueur de connaître sa position et les sorties possibles
        help() : permet au joueur d'obtenir une liste des commandes du jeu
        look() : permet au joueur de connaître les objets et les pnjs dans la pièce
        take() : permet au joueur de prendre un objet
        drop() : permet au joueur de lâcher un objet
        check() : permet au joueur de regarder son inventaire
        talk() : permet au joueur d'intéragir avec les pnjs


    Les exceptions levées par la classe sont :
        None
    """
#------------------------------------
# Prise en compte de la commande vide

# la variable "game" doit être noté pour le bon fonctionnement
# des commande, donc on suspend exceptionnellement le contrôle
# pylint: disable=unused-argument

    @staticmethod
    def nothing(game, list_of_words, number_of_parameters):
        '''

        Objectif :
        Ne pas déclencher une erreur si  le joueur n'écrit rien.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return None

#------------------------------------

    @staticmethod
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

        ### La seconde partie du code permet aux pnjs de bouger de façon aléatoire
            for char in game.all_characters :
                ach = game.all_characters[char]
                # print(r.characters) # test
                if ach.move_or_not == 1 :
                    ach.move()
        else :
            print(MSG2.format(direction=list_of_words[1]))
        return True

#------------------------------------

    @staticmethod
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

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        '''

        Objectif :
        Permet au joueur d'obtenir son historique des pièces visitées.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
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

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        '''

        Objectif :
        Permet au joueur de revenir dans la pièce précédente.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        liste_valeurs = [e for e in player.current_room.exits.values() if e is not None]
        # On récupère uniquement les sorties non vides.

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

    @staticmethod
    def direction(game, list_of_words, number_of_parameters):
        '''

        Objectif :
        Permet au joueur de connaître sa position et les sorties disponibles.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        print(player.current_room.get_long_description())
        return True

#------------------------------------

    @staticmethod
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

    @staticmethod
    def look(game,list_of_words,number_of_parameters):
        '''

        Objectif :
        Permet au joueur de regarder les objets et les pnjs
        qui sont autour de lui.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        print(player.current_room.get_inventory())
        return True

#------------------------------------

    @staticmethod
    def take(game,list_of_words,number_of_parameters):
        '''

        Objectif :
        Permet au joueur de prendre un objet.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        obj_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        if obj_recherche in player.current_room.inventory :
            if obj_recherche not in game.player.inventory.keys() :
                player.inventory[obj_recherche] = player.current_room.inventory[obj_recherche]
            elif obj_recherche in game.player.inventory.keys() :
                player.inventory[obj_recherche].quantity += 1
            petit = player.inventory[obj_recherche].name
            print(f"\n{petit.capitalize()} est maintenant bien au chaud dans ton inventaire.\n")
            del player.current_room.inventory[obj_recherche]
            return True

        print(f"\n{list_of_words[1].capitalize()} n'est pas dans la pièce.\n")
        return False

#------------------------------------

    @staticmethod
    def drop(game,list_of_words,number_of_parameters):
        '''

        Objectif :
        Permet au joueur de lâcher un objet de son inventaire.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        obj_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        if obj_recherche in player.inventory :
            if player.inventory[obj_recherche].drop_or_not == 0 :
                print("\nTu ne vas quand même pas jeter ce souvenir...\n")
                return True

            player.current_room.inventory[obj_recherche] = player.inventory[obj_recherche]
            petit2 = player.inventory[obj_recherche].name
            print(f"\n{petit2.capitalize()} est maintenant sur le sol froid.\n")
            del player.inventory[obj_recherche]
            return True

        print(f"\n{list_of_words[1].capitalize()} n'est pas dans ton inventaire.\n")
        return False

#------------------------------------

    @staticmethod
    def check(game,list_of_words,number_of_parameters):
        '''

        Objectif :
        Permet au joueur de regarder son inventaire.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())
        return None

#------------------------------------

    @staticmethod
    def talk(game,list_of_words,number_of_parameters):
        '''

        Objectif :
        Permet au joueur d'intéragir avec un pnj.

        Arguments :
        game
        list_of_words : liste permettant de comprendre la commande
        number_of_parameters : nombre de paramètre demandé par la commande

        '''
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
        character_recherche = list_of_words[1].upper().translate(table_remplacement).strip()
        if character_recherche in npc_spe and npc_spe[character_recherche] != 0 :
            dlg1 = dialogues[character_recherche]
            get_lines(character_recherche, len(dlg1)-npc_spe[character_recherche])
            npc_spe[character_recherche] -= 1
            return True
        if character_recherche in player.current_room.characters :
            print(player.current_room.characters[character_recherche].get_msg())
            return True

        print("\nHmmmm personne ici ne s'appelle comme ça\n")
        return False

#------------------------------------
