
# voir tata_driver
vie = []
collier = []
dialogues = {'prologue' :
["""Vous êtes dans la peau de Clyde Barrow au galop au milieu du désert, en 1831. Vous êtes actuellement
en fuite et à la recherche d'argent suite à un casse qui à mal tourné. De plus, vous avez perdu votre femme, 
Bonnie Parker, à la suite de celui-ci.

Mais voilà qu'après plusieurs jours à galoper sans arrêt, vous décidez de vous arrêter dans la ville de LuckyLand.

...
...
...

Clyde : Ce petit hôtel fera très bien l'affaire pour me reposer"""],
'fin' :
["""\nSoudain, Clyde vit apparaître Bonnie devant lui, il pleura et voulut la serrer fort dans ses bras mais elle 
disparut. Il se réveilla en sursaut dans la chambre et comprit alors qu’il avait rêvé et que Bonnie avait bel et
bien disparu…\n"""],
'RECEPTIONNISTE' : 
["\nDemande la clé d’une chambre au réceptionniste pour obtenir une chambre", [lambda : input("\nRéceptionniste : Qu’est ce qui est plus grand que la Tour Eiffel, mais infiniment moins lourd ?\n"),
"SON OMBRE", "\nBravo ! Voici la clé de votre chambre, elle est à l'étage."]],
'SHERIF' :
["""\nShérif : Oui, mon cher, je l’ai vu dans la cellule d’un des prisonniers, il passe son temps à le contempler et 
à lui parler.""", 
[lambda : input("""\nShérif : Bien sûr, mais avant il faudra répondre à l’énigme suivante: Qu'est-ce qui n'est pas 
vivant mais qui grandit, n'a pas de poumon mais a besoin d'air, et meurt sous l'eau ?\n"""), 
 "LE FEU","\nShérif : Exact, maintenant tu peux aller voir le prisonnier mais fais attention il mord.", 1]]
,'EXTRATERRESTRE' :
["""\nExtraterrestre : Moi savoir où trouver collier. Collier se trouvait en haut de la colline 
là bas dans temple, vous avoir besoin de 5h de marche. Mais attention là-bas y avoir gardien du temple dangereux."""],
'GARDIEN' :
["""\nGardien du temple : Bonjour étranger, que viens tu faire par ici, ne sais tu pas que c’est dangereux de 
m’approcher, je garde près de moi des objets d'une valeur inestimable.""", 
[lambda : input("\nGardien du temple : Qu'est-ce qui t'appartient mais que les autres utilisent plus que toi ?\n"),
"MON PRENOM", "Bravo, voilà le morceau de collier comme promis", 12]],
'BAKOU' :
["\nBakou : Merci pour ton aide précieuse, en quoi puis-je te venir en aide ?", 
[lambda : input("""Bakou : Je ne l’ai jamais vu ici, mais par contre je pense que tu peux la trouver sur une des deux 
lunes qui gravitent autour de ma planète. Néanmoins, une des deux lunes ne te laissera jamais revenir et tu mourras. 
Pour avoir le luxe d’être guidé il faut que tu répondes correctement à l’énigme suivante : 

Mon premier est une lettre de l’alphabet.
Mon deuxième est un oiseau qui aime tout ce qui brille.
Mon troisième est un talent particulier que l’on peut avoir.
Mon tout a beaucoup de travail le jour de la Saint-Valentin.\n"""), "CUPIDON",
"""\nBakou : C’est la bonne réponse tu vas pouvoir être guidé vers la bonne lune et ainsi pouvoir trouver ton collier.""",
37]],
'JARJARBINKS' :
["\nJar Jar Binks : Bonsoir jeune voyageur, que viens tu faire dans ma ville ?", 
"""\nJar Jar Binks : Tiens donc… tout dépend de l’individu mais l’avenir d’un homme peut se trouver soit dans une
femme, soit dans le travail mais surement pas dans les jeux d’argent. Alors quel genre d’avenir êtes-vous venu chercher ?""",
[lambda : input("""Jar Jar Binks : Hmm je vois, tu es Clyde le célèbre tueur à gage. Je peux t’aider à obtenir ce que 
tu cherches pour te consoler. Mais il faudra répondre à l’énigme suivante : 

Considère la suite de chiffres suivante : 0 1 1 2 3 5 8

Quel chiffre suit le 8 ?\n"""), "13",
"""\nChaque nouveau chiffre est le résultat de l’addition des deux précédents. 
0 + 1 = 1 / 1 + 1 = 2 / 1 + 2 = 3 etc, donc 5 + 8
 
Jar Jar Binks : Bonne réponse, je garde cette pièce de ton collier dans un coffre fort bien scellé. Pour le récupérer,
tu devras jouer à 2 jeux de stratégie contre un maître. Si tu gagnes, le maître te donnera une des mes bagues. Si tu
me l’apportes, le collier est à toi.""", 101]] 
}


def get_lines(name , number=-1) :
    '''Permet d'obtenir les dialogues du jeu'''
    try:
        if number >= 0:
            pluriel = ["tentatives", "tentative"]
            table_remplacement = str.maketrans("ÉÈÀÙÇÊË","EEAUCEE")
            dialogue = dialogues[name][number]
            if callable(dialogue[0]): # Si la première partie est une fonction (comme lambda, la fonction anonyme)
                for i in range (3) :
                    print(dialogue[1])
                    reponse = dialogue[0]()  # Appeler la fonction pour déclencher l'input
                    reponse_ordi = reponse.upper().translate(table_remplacement).strip() # Forme utilisée pour vérifier la réponse
                    if i <= 1 :
                        if reponse_ordi != dialogue[1] :
                            print(f"\nVotre réponse : {reponse}, est mauvaise, encore {2-i} {pluriel[i]}.")
                        elif reponse_ordi == dialogue[1] :
                           print(dialogue[2])
                           if len(dialogue) == 4 :
                               collier.append(dialogue[3])
                               print(f"{collier} , Sommme : {sum(collier)}")
                           return True
                    elif reponse_ordi == dialogue[1] :
                        print(dialogue[2])
                        if len(dialogue) == 4 :
                            collier.append(dialogue[3])
                            print(f"{collier} , Sommme : {sum(collier)}")
                        return True
                    else :
                        print("\nVous n'êtes plus le bienvenu ici monsieur, au revoir.\n\n\nVous avez perdu...")
                        vie.append(1)
                        return False
            else:
                print(dialogues[name][number])  # Sinon, afficher directement le dialogue du PNJ
            return True
        else:
            print("--- Si ce message apparaît, une erreur s'est produite --- (line, dial) ")
            return False
    except KeyError:
        print(f"--- Si ce message apparaît, une erreur s'est produite --- (line, key) ")
        return False

