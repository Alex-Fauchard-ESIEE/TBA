
# voir tata_driver
vie = []
dialogues = {'prologue' :
    ["""Vous êtes dans la peau de Clyde Barrow au galop au milieu du désert, en 1831. Vous êtes actuellement
en fuite et à la recherche d'argent suite à un casse qui à mal tourné. De plus, vous avez perdu votre femme, Bonnie 
Parker, à la suite de celui-ci.\n\n
Mais voilà qu'après plusieurs jours à galoper sans arrêt, vous décidez de vous arrêter dans la petite ville de LuckyLand.
\n...\n...\n...\n
Clyde : Ce petit hôtel fera très bien l'affaire pour me reposer"""], 
'RECEPTIONNISTE' : [[lambda : input("\nRéceptionniste : Qu’est ce qui est plus grand que la Tour Eiffel, mais infiniment moins lourd ?\n"), "LA TOUR EIFFEL", "\nBravo !"]],
}
def get_lines(name , number=-1) :
    '''Permet d'obtenir les dialogues du jeu'''
    try:
        if number >= 0:
            dialogue = dialogues[name][number]
            if callable(dialogue[0]): # Si la première partie est une fonction (comme lambda, la fonction anonyme)
                for i in range (3) :
                    reponse = dialogue[0]()  # Appeler la fonction pour déclencher l'input
                    if i <= 1 :
                        if reponse != dialogue[1] :
                            print(f"\nVotre réponse : {reponse}, est mauvaise, encore {2-i} tentatives.")
                        elif reponse == dialogue[1] :
                           print(dialogue[2]) 
                    elif reponse == dialogue[1] :
                        print(dialogue[2])
                    else :
                        print("\nVous n'êtes plus le bienvenu ici monsieur, au revoir.\n\n\nVous avez perdu...")
                        vie.append(1)
            else:
                print(dialogues[name][number])  # Sinon, afficher directement
            return True
        else:
            print(" --- Si vous voyez ce message, alors une erreur est survenue dans le chargement des dialogues --- ")
            return False
    except KeyError:
        print(f" --- Le personnage : {name}, n'existe pas dans les dialogues --- ")
        return False
