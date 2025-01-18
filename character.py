import random
class Character():

    def __init__(self, name, description, current_room, msgs, zone, move_or_not):
        '''
        move_or_not : peut bouger s'il vaut 1
        zone : 1 ou 2 selon l'endroit ou le pnj peut se déplacer
        '''
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.zone = zone
        self.move_or_not = move_or_not
        self.bag = {}

#------------------------------------

    def __str__(self):
        return f"{self.name} : {self.description}"

#------------------------------------

    def move(self):
        l = [0,1]
        n = random.choice(l)
        temp = self.current_room
        if n == 1 :
            exits_adj = [value for value in list(self.current_room.exits.values()) if value != None]
            piece_adj = random.choice(exits_adj)
            if self.zone == piece_adj.zone :
                self.current_room = piece_adj
                #print(f"{self.name} avant : {temp.name} avec {temp.characters} et après : {self.current_room.name} avec {self.current_room.characters} ")
                self.current_room.characters[self.name.upper()] = temp.characters[self.name.upper()]
                del temp.characters[self.name.upper()]
                return True
        else :
            return False

#------------------------------------

    def get_msg(self) :
        #print(self.msgs, type(self.msgs)) # test
        if self.msgs != [] : #not in ([] , [0]) :
                msg = self.msgs.pop(0)
                self.msgs.append(msg)
                return msg
        #elif self.msgs == []  :
            #return f"{self.name} n'a plus rien à vous dire..."
        elif self.msgs == [] :
            return f"{self.name} n'a vraisemblablement rien à vous dire..."
        else :
            return False

    
    def give(game, self) :
            if self.bag == [] :
                print("--- Si ce message apparaît, une erreur s'est produite --- (give)")
            else :
                obj = self.bag[0]
                game.self = self
                game.player.inventory[self.bag[0].name] = [self.bag[0]]
                print(f"Vous avez récupéré : {self.bag[0].name.capitalize()}, dans votre inventaire")