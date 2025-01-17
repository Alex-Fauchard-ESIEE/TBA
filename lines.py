
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

'Perle' :
["""\nClyde : Maintenant, je vais aller siroter un gin dans ma chambre pour me déshydrater ! 
@ Vous vous endormez @

...
...
...

@ Au réveil, vous voyez quelque chose de brillant dans le meuble @

Clyde : Mais je reconnais ce morceau de collier abimé, c’est celui de Bonnie ! Si seulement je n'avais pas perdu Bonnie pendant ce braquage de 2nde zone…"""],

'Bar' :
["""\n @ D’une mine triste et désemparée, Clyde alla au saloon d’en face et bu jusqu’à l’aube.
Vous vous réveillez complètement ivre @

Clyde : Mais que fais-je au milieu de la rue alors que j’étais au saloon ? Je vais trouver le reste du collier pour retrouver Bonnie !"""],

'RECEPTIONNISTE' : 
[[lambda : input("\nClyde : Bonjour, auriez-vous une chambre de libre ?\n\nRéceptionniste : Bonjour, oui mais avant vous allez devoir me répondre. Qu’est ce qui est plus grand que la Tour Eiffel,\n mais infiniment moins lourd ?\n"),
"SON OMBRE", "\nBravo ! Voici la clé de votre chambre, elle est à l'étage."]],
'SHERIF' :
["\nClyde : Bonjour shérif, savez-vous où est-ce que je peux trouver un morceau de collier similaire à celui-ci ? \n\nShérif : Oui, mon cher, je l’ai vu dans la cellule d’un des prisonniers, il passe son temps à le contempler et à lui parler.",
[lambda : input("""\nClyde : Puis-je rendre visite à cet individu ?\n\nShérif : Bien sûr, mais avant il faudra répondre à l’énigme suivante: 
Qu'est-ce qui n'est pas vivant mais qui grandit, n'a pas de poumon mais a besoin d'air, et meurt sous l'eau ?\n"""), 
 "LE FEU","\nShérif : Exact, maintenant tu peux aller voir le prisonnier mais fais attention il mord.","\nClyde : Il va goûter à mes tatanes!","\n@ Vous lui lancer un coup de pied qui l’endort pour quelques temps.@","\nClyde : Mais de toute façon je ne la retrouverai jamais...", 1]],
'Chappelle' :
["\nClyde : Tous mes espoirs sont perdus, je vais finir cette bouteille de gin pour oublier puis aller prier…","\nClyde : Je vais m’installer dans le confessionnal pour prier", 
"""\n @ Vous vous endormez 
...
...
...@ """ 

"""\nClyde: 
Wooow, mais où suis-je !

Je distingue de grosses boules autour de moi, des points brillant, le reste n’est que du noir à n’en plus finir, finalement je distingue des êtres un peu bizarres.

Ahhh voilà des panneaux, je suis donc sur la planète Kapry, et apparemment les êtres parlent la même langue que moi !

Bonjour Monsieur, je cherche un morceau de collier qui ressemblerait à celui là.""", 
"""\nExtraterrestre : Moi savoir où trouver collier. Collier se trouvait en haut de la colline là bas dans temple, vous avoir besoin de 5h de marche. Mais attention là-bas y avoir gardien du temple dangereux.""",
"\n@ Peu après l'explication de l’extraterrestre fort aimable, vous vous mettez à marcher en direction du sommet de la colline jusqu’à atteindre le temple et par conséquent le gardien. @"],
["\nShérif : Oui, mon cher, je l’ai vu dans la cellule d’un des prisonniers, il passe son temps à le contempler et à lui parler.",
[lambda : input("""\nShérif : Bien sûr, mais avant il faudra répondre à l’énigme suivante: Qu'est-ce qui n'est pas 
vivant mais qui grandit, n'a pas de poumon mais a besoin d'air, et meurt sous l'eau ?\n"""), 
 "LE FEU","\nShérif : Exact, maintenant tu peux aller voir le prisonnier mais fais attention il mord.", 1]]
,'EXTRATERRESTRE' :
["""\nExtraterrestre : Moi savoir où trouver collier. Collier se trouvait en haut de la colline 
là bas dans temple, vous avoir besoin de 5h de marche. Mais attention là-bas y avoir gardien du temple dangereux."""],
'GARDIEN' :
["""\nGardien du temple : Bonjour étranger, que viens tu faire par ici, ne sais tu pas que c’est dangereux de m’approcher, je garde près de moi des objets d'une valeur inestimable.""",
"\nClyde: Je sais… oh tout puissant gardien mais je viens quand même demander avec toute ma reconnaissance si vous pouviez me donner la partie du collier qui ressemble à celui dont j’ai trouvé des morceaux.",
"\n@ Vous racontez au gardien l’histoire émouvante du collier et de Bonnie, le gardien ému vous propose une énigme que vous devez à tout prix réussir pour avoir le collier.@"
,[lambda : input("\nGardien du temple : Qu'est-ce qui t'appartient mais que les autres utilisent plus que toi ?\n"),
"MON PRENOM", "Bravo, voilà le morceau de collier comme promis", 12]],
'Minto' :
["\n@ Sur Minto, vous faites la rencontre d’une tribu de gorilles sauvage et violente qui ne comprend que les mimes. Vous sympathisez avec leur chef Bakou qui vous emmène chasser la gazelle avec eux. Bakou reconnut les talents de chasse de Clyde.@"],
'BAKOU' :
["\nBakou : Merci pour ton aide précieuse, en quoi puis-je te venir en aide ?","\nClyde : Je suis à la recherche de pièces de collier ressemblant à celui-ci. Par hasard, est-ce que tu aurais vu traîner cette pièce quelque part ?",
[lambda : input("""Bakou : Je ne l’ai jamais vu ici, mais par contre je pense que tu peux la trouver sur une des deux 
lunes qui gravitent autour de ma planète. Néanmoins, une des deux lunes ne te laissera jamais revenir et tu mourras. 
Pour avoir le luxe d’être guidé il faut que tu répondes correctement à l’énigme suivante : 

Mon premier est une lettre de l’alphabet.
Mon deuxième est un oiseau qui aime tout ce qui brille.
Mon troisième est un talent particulier que l’on peut avoir.
Mon tout a beaucoup de travail le jour de la Saint-Valentin.\n"""), "CUPIDON",
"""\nBakou : C’est la bonne réponse tu vas pouvoir être guidé vers la bonne lune et ainsi pouvoir trouver ton collier.""",
"\nClyde : Merci, Bakou.",37]],
'Jafar' :
["""\n@ Vous êtes guidé par un singe à l’allure fort étrange et vous finissez par arriver sur la lune Litchi, vous y trouvez de la végétation à foison. Au milieu des arbres, vous apercevez un sanctuaire où reposait une partie du collier de Bonnie. 
Clyde arriva sur Jafar, sur cette planète pleine de dunes de sable, Clyde aperçut une ville Casino Land la ville du jeu. Dans cette ville, on pouvait y trouver toutes sortes d’espèces : des extraterrestres, des singes, des gorilles, des humanoïdes … 
Clyde s’assit à une table de poker, et fit la connaissance du maître des lieux  : Jar Jar Binks.@"""],
'JARJARBINKS' :
["\nJar Jar Binks : Bonsoir jeune voyageur, que viens tu faire dans ma ville ?\n\nClyde : Je suis à la recherche de mon avenir.", 
"""\nJar Jar Binks : Tiens donc… tout dépend de l’individu mais l’avenir d’un homme peut se trouver soit dans une
femme, soit dans le travail mais surement pas dans les jeux d’argent. Alors quel genre d’avenir êtes-vous venu chercher ?"""

"""\nClyde : Je suis à la recherche du dernier morceau de collier de ma femme disparue, Bonnie.""",
[lambda : input("""\nJar Jar Binks : Hmm je vois, tu es Clyde le célèbre tueur à gage. Je peux t’aider à obtenir ce que 
tu cherches pour te consoler. Mais il faudra répondre à l’énigme suivante : 

Considère la suite de chiffres suivante : 0 1 1 2 3 5 8

Quel chiffre suit le 8 ?\n"""), "13",
"""\nChaque nouveau chiffre est le résultat de l’addition des deux précédents. 
0 + 1 = 1 / 1 + 1 = 2 / 1 + 2 = 3 etc, donc 5 + 8."""
 
"""\nJar Jar Binks : Bonne réponse, je garde cette pièce de ton collier dans un coffre fort bien scellé. Pour le récupérer,
tu devras jouer à 2 jeux de stratégie contre un maître. Si tu gagnes, le maître te donnera une des mes bagues. Si tu
me l’apportes, le collier est à toi.""","\nClyde : Je réussirai et je remporterai le dernier bout de collier.", 101]] 
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
