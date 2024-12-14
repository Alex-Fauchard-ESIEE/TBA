class Character():

#Define the constructor
def __init__(self,name):
    self.name = name
    self.description = []
    self.current_room = []
    self.msgs = []


def __str__(self):
        return f"{self.name} : {self.description}"

