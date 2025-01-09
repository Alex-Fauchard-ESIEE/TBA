import random
class Character():

    def __init__(self, name, description, current_room, msgs, move_or_not):
        '''
        move_or_not : peut bouger si il vaut 1
        '''
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.bag = {}
        self.move_or_not = move_or_not

#------------------------------------

    def __str__(self):
        return f"{self.name} : {self.description}"

#------------------------------------

    def move(self):
        l = [0,1]
        n = random.choice(l)
        if n == 1 :
            exits_adj = [value for value in list(self.current_room.exits.values()) if value != None]
            piece_adj = random.choice(exits_adj)
            self.current_room = piece_adj
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