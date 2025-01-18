"""La classe Game est la classe centrale du jeu qui permet de construir celui-ci
et de le faire fonctionner."""


# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from lines import get_lines, depart, vie, collier, tp

# Le nombre d'attributs, de variables locales et de conditions est forcément
# élevé, voir très élevé, dans la construction de Game. Ainsi, on retire les
# contrôles s'appliquant à tout ça.
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

class Game:
    """
        Cette classe au jeu de fonctionner.

        une description plus détaillée de la classe ;

        Les attributs de la classe sont :
            finished : permet d'interompre le jeu
            rooms : liste des pièces du jeu
            player : joueur
            sorties_valides : set de toutes les sorties valides des pièces du jeu
            all_characters : dictionnaire de tous les pnjs du jeu {str : Character}
            gin, ivre : constantes permettant de déclencher des évènements

        Les méthodes de la classe sont : 
            __init__() : constructeur
            setup() : permet de créer tous ce qu'il faut pour le jeu
            play() : permet de lancer le jeu et le faire fonctionner
            process_command() : permet de prendre en charge les commandes
            print_welcome() : permet de lancer le début du jeu

        Les exceptions levées par la classe sont :
            None
    """
#------------------------------------

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.sorties_valides = set()
        self.all_characters = {}
        self.gin = 1
        self.ivre = 1

#------------------------------------

    # Setup the game

    # Les commandes "quit" et "help" doivet exister, mais pylint refuse
    # car ce sont des mots utiliser dans python lui-même. Ainsi, on
    # désactive exceptionnellement le contrôle.
    # pylint: disable=redefined-builtin
    def setup(self):
        '''

        Objectif :
        Permet de créer tous ce qu'il faut pour le jeu.

        Argument :
        self

        '''
        # Setup commands
        help = Command("help",
                       " : afficher cette aide",
                       Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit",
                       " : quitter le jeu",
                       Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go",
        " <direction> : se déplacer dans une direction cardinale et l'altitude (N, E, S, O, U, D)", 
                     Actions.go, 1)
        self.commands["go"] = go
        nothing = Command('',
                          "'' : la commande vide ne fait rien", 
                          Actions.nothing, 0)
        self.commands[""] = nothing
        history = Command("history",
                          " : afficher le chemin parcouru depuis le début du jeu", 
                          Actions.history, 0)
        self.commands["history"] = history
        back = Command("back",
                       " : retourner au lieu précédent, si cela est possible",
                       Actions.back, 0)
        self.commands["back"] = back
        direction = Command("direction",
                            " : donne votre position et les sorties possibles",
                            Actions.direction, 0)
        self.commands["direction"] = direction
        look = Command("look",
                       " : chercher des objets et des personnes dans la pièce",
                       Actions.look, 0)
        self.commands["look"] = look
        take = Command("take",
                       " <objet> : prendre un objet dans la pièce",
                       Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop",
                       " <objet> : lâcher un objet de son inventaire",
                       Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check",
                        " : jeter un oeil à son inventaire",
                        Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk <character>",
                       " : Parler au personnage",
                       Actions.talk, 1)
        self.commands["talk"] = talk

        # Setup rooms
        rue = Room("Rue principale",
"Je suis dans une rue de western avec ses chevaux, ses cowboys et ses douilles au sol.", 1)
        self.rooms.append(rue)
        saloon = Room("Saloon",
        "Ce bon vieux saloon ne m'est plus accessible car le gérant m'a viré.", 1)
        self.rooms.append(saloon)
        prison = Room("Bureau du shérif",
        "Le shérif est toujours là, histoire de veiller sur cette charmante petite ville.", 1)
        self.rooms.append(prison)
        chapelle = Room("Chapelle",
        "La chappelle est calme, je vois un hôtel au fond et un confessionnal à ma gauche.", 1, 1)
        self.rooms.append(chapelle)
        hotel = Room("Hotel",
"""Je suis dans l'entrée de l'hôtel, un réceptionniste me fait face derrière le comptoir et
je vois un escalier au fond.""", 1)
        self.rooms.append(hotel)
        etage = Room("Étage",
        "Dans ce couloir mal éclairé, il y a 3 chambres, et de multiples objets au sol.", 1)
        self.rooms.append(etage)
        chambre1 = Room("Chambre 1",
        "Une chambre tout à fait banal, avec une petite fenêtre donnant sur la rue principale", 1)
        self.rooms.append(chambre1)
        chambre2 = Room("Chambre 2",
"""Cette chambre vient vraisemblablement d'être quittée en vitesse, il reste encore de 
nombreux objets un peu partout.""", 1)
        self.rooms.append(chambre2)
        chambre3 = Room("Chambre 3",
"Ça ne ressemble plus vraiment à une chambre mais plutôt un débarras ici.", 1)
        self.rooms.append(chambre3)
        zany = Room("Zany",
"Cette lune me semble assez austère, elle ressemble un peu au désert que je connais bien.", 2)
        self.rooms.append(zany)
        litchie = Room("Litchie",
"""Je suis entouré de végétation largement plus grande que moi, au point que je ne vois déjà presque
plus mon vaisseau après quelques mètres. Mais il y a des traces de vie autour de moi.""", 2)
        self.rooms.append(litchie)
        kapry = Room("Kapry",
"""Ici la fête est partout et les gens sont déchaînés, je ne sais pas si je vais rester longtemps.
À moins qu'il n'y ait un petit marché pas loin !""", 2)
        self.rooms.append(kapry)
        temple = Room("Temple",
        "Cet endroit est majestueux et semble cacher de nombreux trésors !", 2)
        self.rooms.append(temple)
        pandora = Room("Pandora",
"""Cette planète peuplée d'humanoide me terrifie, elle est surprenante de par ses constructions
originales et son ciel obscur.""", 2)
        self.rooms.append(pandora)
        jafar = Room("Jafar",
"""Cette planète a un paysage plutôt désertique avec de vastes étendue de dunes de sables,
on peut apercevoir une grande ville luxueuse appelée "Casino Land""", 2, 1)
        self.rooms.append(jafar)
        minto = Room("Minto",
""""Ici prospère un calme absolu, le seul bruit que j'entend est celui des vagues qui s'échoue
sur cette petite île paradisiaque entourée d'eau, tout comme le reste de la planète """, 2, 1)
        self.rooms.append(minto)
        pollux = Room("Pollux",
"""Une lune des plus déconcertante chacun de mes pas est un supplice dû aux poils longs et
marrons se trouvant sur le sol, ces poils proviennent des nuages""", 2)
        self.rooms.append(pollux)
        sid = Room("Sid",
"""Le paysage de cette lune est celui de vastes plaines vertes et de plantes, néanmoins l'air
de l'atmosphère insufflé après chaque respiration me donne envie de dormir, mais je dois lutter
pour rejoindre le fameux temple sacré des dormeurs.""", 2)
        self.rooms.append(sid)
        tancoeur = Room("Tancoeur",
"""Cette planète semble refusé ma présence, moi qui suit allergique à la désolation,
celle-ci est composé de pierres sombres, de montagnes noires et de volcans""", 2)
        self.rooms.append(tancoeur)
        isoloir = Room("Isoloir",
        "Petite pièce de la chapelle servant normalement à se recueillir", 1, 1)
        self.rooms.append(isoloir)

        # Create exits for rooms
        rue.exits = {"N" : saloon, "E" : hotel, "S" : None, "O" : prison, "U" : None, "D" : None}
        saloon.exits = {"N" : None, "E" : None, "S" : rue, "O" : None, "U" : None, "D" : None}
        prison.exits = {"N" : None, "E" : rue, "S" : None, "O" : None, "U" : None, "D" : None}
        chapelle.exits = {"N" : rue, "E" : None, "S" : None, "O" : isoloir, "U" : None, "D" : None}
        hotel.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        etage.exits = {"N" : chambre1,
                       "E" : chambre2,
                       "S" : chambre3,
                       "O" : None,
                       "U" : None,
                       "D" : hotel}
        chambre1.exits = {"N" : None, "E" : None, "S" : etage, "O" : None, "U" : None, "D" : None}
        chambre2.exits = {"N" : None, "E" : None, "S" : None, "O" : etage, "U" : None, "D" : None}
        chambre3.exits = {"N" : etage, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        zany.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : minto}
        litchie.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : minto, "D" : None}
        minto.exits = {"N" : None, "E" : kapry, "S" : None, "O" : jafar, "U" : zany, "D" : litchie}
        kapry.exits = {"N" : None, "E" : None, "S" : temple, "O" : None, "U" : None, "D" : None}
        temple.exits = {"N" : kapry, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        jafar.exits = {"N" : None, "E" : None, "S" : None, "O" : pandora , "U" : pollux, "D" : sid}
        tancoeur.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : pandora}
        sid.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : jafar}
        pollux.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : jafar}
        pandora.exits = {"N" : None,
                         "E" : None,
                         "S" : None,
                         "O" : kapry,
                         "U" : tancoeur,
                         "D" : None}
        isoloir.exits = {"N" : None,
                         "E" : chapelle,
                         "S" : kapry,
                         "O" : None,
                         "U" : None,
                         "D" : None}

        # Setup sets for room's exits
        for e in self.rooms :
            self.sorties_valides = self.sorties_valides | set(e.exits.keys())

        # Setup items for rooms
        douilles = Item("Douilles", "Un tas de douilles", 18)
        rue.inventory["DOUILLES"] = douilles
        perle = Item("Perle",
"C'est un morceau du collier que j'avais offert à Bonnie lors de notre rencontre", 1, 0)
        chambre1.inventory["PERLE"] = perle
        montre = Item("Montre", "une montre usée", 1)
        chambre2.inventory["MONTRE"] = montre
        lunettes = Item("Lunettes", "tout ce qu'il y a de plus banal", 1)
        chambre2.inventory["LUNETTES"] = lunettes
        bottes = Item("Bottes", "De véritable bottes de cowboy !", 2)
        chambre2.inventory["BOTTES"] = bottes
        draps = Item("Draps", "Des draps pour matelas", 3)
        chambre3.inventory["DRAPS"] = draps
        bois = Item("Bois", "Quelques bâtons de bois", 8)
        chambre2.inventory["BOIS"] = bois
        cailloux = Item("Cailloux", "Vraiment ??? Tu veux que je décrive des cailloux ?", 37)
        rue.inventory["CAILLOUX"] = cailloux
        affiches = Item("Affiches", "Ce sont les affiches des gens recherchés", 3)
        prison.inventory["AFFICHES"] = affiches
        bible = Item("Bible", "C'est la bible du prêtre", 1)
        chapelle.inventory["BIBLE"] = bible
        crucifix = Item("Crucifix", "On dirait du bronze", 1)
        chapelle.inventory["CRUCIFIX"] = crucifix
        pieces = Item("Pieces", "Ça doit être la monnaie sur Jafar", 6)
        jafar.inventory["PIECES"] = pieces
        totem = Item("Totem", "c'est une pièce du trésor du temple", 1)
        temple.inventory["TOTEM"] = totem
        cailloux = Item("Cailloux", "Encore des cailloux, sérieusement ??", 2)
        zany.inventory["CAILLOUX"] = cailloux

        # Setup PNJs for rooms
        alien = Character("Alien", " Un vrai petit bonhommme vert", zany,
        ["\n Alien : Zougizi dicurta prodo !\n", "\n Alien : Pona mioutu azcho\n"], 1, 0)
        zany.characters["ALIEN"] = alien
        bob = Character("Bob", "un gars lambda", rue, ["\nBob : Bonjour monsieur\n"], 1, 1)
        rue.characters["BOB"] = bob
        receptionniste = Character("Receptionniste", 'un petit gars banal', hotel,
        ["\nRéceptionniste : Je n'ai malheureusement pas de chambre disponible\n"], 1, 0)
        hotel.characters["RECEPTIONNISTE"] = receptionniste
        sherif = Character("Shérif", "Le héro qui protège la ville !", prison,
        ["\n Shérif : Je n'ai aucun travail pour vous monsieur\n"], 1, 0)
        prison.characters["SHERIF"] = sherif
        extraterrestre = Character("Extraterrestre",
        "Une créature un peu bizarre mais dont je comprends la langue", kapry,
        ["\nExtraterrestre : ...\n"], 2, 0)
        kapry.characters["EXTRATERRESTRE"] = extraterrestre
        gardien = Character("Gardien",
        "Ce personnage est intimand mais amical", temple,
        ["\nGardien : Vous ne devriez pas rester ici monsieur\n"], 2, 0)
        temple.characters["GARDIEN"] = gardien
        bakou = Character("Bakou",
"Ce gorille semble être le chef de la tribu, mais il ne parle pas ma langue",
minto, ["\nBakou : ...\n"], 2, 0)
        minto.characters["BAKOU"] = bakou
        jarjarbinks = Character("JarJarBinks",
        "Cette drôle de créature semble tout droit sortie d'un film !",
        jafar, ["\nJarJarBinks : Meesa s'appelle JarJarBinks\n"], 2, 0)
        jafar.characters["JARJARBINKS"] = jarjarbinks
        barman = Character("Barman", "Ce monsieur n'a pas l'air de beaucoup m'apprécié",
saloon, ["\nBarman : Sortez de mon saloon et ne revenez plus jamais !\n"], 1, 0)
        saloon.characters["BARMAN"] = barman
        prisonnier = Character("Prisonnier", "Il ne fait pas très peur pour un voyou", prison,
        ["\n@ Vous devez avoir l'autorisation du shérif pour lui parler @\n"], 1, 0)
        prison.characters["PRISONNIER"] = prisonnier
        cowboy = Character("Cowboy", "Un brave type un peu trop confiant", rue,
        ["\nCowboy : Heyyyyy !\n",
        "\nCowboy : Attention monsieur je suis un as de la gâchette !\n"], 1, 1)
        rue.characters["COWBOY"] = cowboy
        ivrogne = Character("Ivrogne", "en train de dormir sur le sol", rue,
        ["\nIvrogne : Rrrrrr\n", "\nIvrogne : Hmmmmm\n"], 1, 0)
        rue.characters["IVROGNE"] = ivrogne
        chien = Character("Chien", "un toutou plein d'énergie", prison,
        ["\nChien : Wouaf !\n", "\nChien : Grrrrr\n"], 1, 1)
        prison.characters["CHIEN"] = chien
        pretre = Character("Prêtre", "un gentil monsieur dévoué", chapelle,
        ["\nPrêtre : Bonjour mon frère\n",
        "\nPrêtre : Ayez toujours la foi, cela vous aidera\n"], 1, 0)
        chapelle.characters["PRETRE"] = pretre
        vendeur = Character("Vendeur", "un jeune homme sympathique", rue,
        ["\nVendeur : Qui veut un journal ?\n", "\nVendeur : Le journal du jour !\n"], 1, 0)
        rue.characters["VENDEUR"] = vendeur
        etranger = Character("Etranger", "Vraisemblablement un mexicain perdu", rue,
        ["\nÉtranger : Holà !\n"], 1, 1)
        rue.characters["ETRANGER"] = etranger
        singe = Character("Singe", "Je pense qu'il s'est trompé de planète", kapry,
        ["\nSinge : Ouistitiiiii\n"], 2, 1)
        kapry.characters["SINGE"] = singe
        krikolo = Character("Krikolo", "Une sorte d'humanoïde un peu fou", tancoeur,
["\nKrikolo : Oh un nouveau ! Bienvenu sur Tancoeur l'ami !\n",
 "\nKrikolo : Je suis sûr que vous allez adorer notre lune !\n"], 2, 0)
        tancoeur.characters["KRIKOLO"] = krikolo
        combattant = Character("Combattant", "lui me fait très peur", pandora,
["\nCombattant : Si vous restez trop longtemps je m'occupe de vous\n"], 2, 0)
        pandora.characters["COMBATTANT"] = combattant
        touriste = Character("Touriste", "celui-là a l'air aussi perdu que moi", minto,
        ["\nTouriste : Bonjour !\n", "\nTouriste : Vous ne ressemblez pas au locaux...\n"], 2, 1)
        minto.characters["TOURISTE"] = touriste
        carouli = Character("Carouli", "Apparement c'est la star du casino local ", jafar,
        ["\nCarouli : Une partie ?\n",
        "\nCarouli : Je n'ai pas encore perdu aujourd'hui !\n"], 2, 0)
        jafar.characters["CAROULI"] = carouli
        maximus = Character("Maximus", "Un voyou raté dont tous le monde se moque", sid,
        ["\nMaximus : Un jour vous me craindrez tous !\n"], 2, 1)
        sid.characters["MAXIMUS"] = maximus
        bioman = Character("Bioman", "On se demande ce qu'il fait ici lui", pollux,
        ["\nBioman : Moitié Homme, moitié Robot !\n"], 2, 0)
        pollux.characters["BIOMAN"] = bioman

        # Setup the dict of all characters
        for r in self.rooms :
            for char in r.characters :
                self.all_characters[char] = r.characters[char]

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        Player.name = self.player
        self.player.current_room = hotel
        self.player.inventory = {}
        self.player.character = {}

#------------------------------------

    # Beginning of history

    # Play the game
    def play(self):
        '''

        Objectif :
        Permet de lancer le jeu et le faire fonctionner.

        Argument :
        self

        '''
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            spcr = self.player.current_room
            spi = self.player.inventory
            if sum(collier) == 1 :
                maillon = Item("Maillon",
"C'est un maillon en or, un morceau du collier que j'avais offert à Bonnie", 1, 0)
                self.player.inventory["MAILLON"] = maillon
                print("\n@ Vous avez reçu un objet @\n")
                self.rooms[0].exits["S"] = self.rooms[3]
                print("@ La porte de la chapelle est maintenant ouverte @\n")
                collier.append(1)
            elif sum(collier) == 14 :
                pierre = Item("Pierre",
"C'est encore un morceau du collier que j'avais offert à Bonnie", 1, 0)
                self.player.inventory["PIERRE"] = pierre
                print("\n@ Vous avez reçu un objet @\n")
                self.rooms[11].exits["O"] = self.rooms[15]
                self.rooms[11].exits["E"] = self.rooms[13]
                print("@ Pandora et Minto sont désormais accessibles @\n")
                collier.append(1)
            elif sum(collier) == 52 :
                chaine = Item("Chaîne",
                "C'est un maillon en argent, encore une partie du collier", 1, 0)
                self.player.inventory["CHAINE"] = chaine
                print("@ Vous avez reçu un objet @\n")
                self.rooms[15].exits["O"] = self.rooms[14]
                print("@ Vous pouvez maintenant visiter Jafar ! @\n")
                collier.append(1)
            elif sum(collier) == 154 :
                pendentif = Item("Pendentif",
                "Et voilà la dernière pièce pour reconstituer le collier !", 1, 0)
                self.player.inventory["PENDENTIF"] = pendentif
                print("\n@ Vous avez reçu le dernier morceau du collier de Bonny @\n")
                get_lines('fin', 0)
                self.finished = True
            if len(vie) != 0 :
                self.finished = True
            if spcr == self.rooms[6] and self.gin == 1 :
                get_lines('Perle', 0)
                self.gin = 0
            if spcr == self.rooms[6] and self.ivre == 1 and "PERLE" in spi :
                get_lines('Bar', 0)
                self.player.current_room = self.rooms[0]
                self.ivre = 0
                print(self.player.current_room.get_long_description())
                print("""
@ Vous n'avez plus accès au salon à cause de votre comportement @\n""")
                self.rooms[0].exits["N"] = None
                self.rooms[4].exits["O"] = self.rooms[0]
            if self.player.current_room.talk == 1 :
                get_lines(self.player.current_room.name, 0)
                self.player.current_room.talk = 0
                if sum(tp) == 1 :
                    self.player.current_room = self.rooms[11]
                    print(self.player.current_room.get_long_description())
                    tp.remove(1)
            if sum(depart) == 1 and sum(vie) == 0 :
                self.rooms[4].exits["U"] = self.rooms[5]
                print("\n@ Vous pouvez maintenant aller à l'étage ! @\n")
                depart.remove(1)

#------------------------------------

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        '''

        Objectif :
        Permet de prendre en charge les commandes.

        Arguments :
        self
        command_string (str)

        '''
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands:
            print(f"""
Commande '{command_word}' non reconnue.
Entrez 'help' pour voir la liste des commandes disponibles.\n""")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

#------------------------------------

    # Print the welcome message
    def print_welcome(self):
        '''

        Objectif :
        Permet de lancer le début du jeu.

        Argument :
        self

        '''
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        print(f"\n\n{self.player.name} posons le contexte :\n")
        get_lines('prologue', 0)
        print(self.player.current_room.get_long_description())

#------------------------------------

def main():
    '''
    Objectif :
    Create a game object and play the game.

    Argument :
    self

    '''
    Game().play()

if __name__ == "__main__":
    main()
