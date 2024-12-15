import random
class Character():

    def __init__(self, name, description, current_room, msgs, move_or_not):
        '''
        move_or_not : peut bouger si il vaut 1'''
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
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
        if self.msgs != [0] :
            for i in range (len(self.msgs)) :
                return self.msgs.pop(i)
        elif self.msgs == [] :
            return "Il n'a plus rien à vous dire..."
        elif self.msgs == [0] :
            return "Il n'a vraisemblablement rien à vous dire..."