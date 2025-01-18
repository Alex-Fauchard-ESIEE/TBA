"""La classe Character donne des caractéristiques aux personnages et
    permet d'intéragir avec eux."""
import random

# Pour le bon fonctionnement du jeu il n'est pas possible de diminuer
# le nombre de paramètre de la classe. On désactive donc exceptionnellement le contrôle
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
class Character():
    """
    La classe Character donne des caractéristiques aux personnages et
    permet d'intéragir avec eux.

    une description plus détaillée de la classe ;

    Les attributs de la classe sont :
        name : nom de la pièce
        description : une description de la pièce
        current_room : pièce actuelle du pnj
        message : dialogues classiques du pnj
        zone : zone de la map à laquelle le pnj appartient (1 ou 2)
        move_or_not : permet de savoir si le pnj peut se déplacer (0 : non)

    Les méthodes de la classe sont : 
        __init__() : constructeur
        __str__() : permet de redéfinir le print()
        move() : permet de faire se déplacer le pnj
        get_msg() : permet d'obtenir les dialogues classique du pnj

    Les exceptions levées par la classe sont :
        None

    """

#------------------------------------

    def __init__(self, name, description, current_room, msgs, zone, move_or_not):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.zone = zone
        self.move_or_not = move_or_not

#------------------------------------

    def __str__(self):
        return f"{self.name} : {self.description}"

#------------------------------------

    def move(self):
        '''

        Objectif :
        Déplacer le pnj.

        Arguments :
        self

        '''
        l = [0,1]
        n = random.choice(l)
        temp = self.current_room
        if n == 1 :
            exits_adj = [value for value in list(temp.exits.values()) if value is not None]
            piece_adj = random.choice(exits_adj)
            if self.zone == piece_adj.zone :
                self.current_room = piece_adj
                self.current_room.characters[self.name.upper()] = temp.characters[self.name.upper()]
                del temp.characters[self.name.upper()]
                return True
        return False

#------------------------------------

    def get_msg(self) :
        '''

        Objectif :
        Obtenir les dialogues classiques du pnj.

        Arguments :
        self

        '''
        if self.msgs != [] : #not in ([] , [0]) :
            msg = self.msgs.pop(0)
            self.msgs.append(msg)
            return msg
        return f"\n{self.name} n'a vraisemblablement rien à vous dire...\n"
