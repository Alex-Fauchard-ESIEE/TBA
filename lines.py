from player import Player

# voir tata_driver

def get_lines(number) :

    if number == 1 :
        print("\nEntrez 'help' si vous avez besoin d'aide.")
        print(f"\n\n\n{Player.name} posons le contexte :\n")
        print("""Vous êtes dans la peau de Clyde Barrow au galop au milieu du désert, en 1831. Vous êtes actuellement
en fuite et à la recherche d'argent suite à un casse qui à mal tourné. De plus, vous avez perdu votre femme, Bonnie 
Parker, à la suite de celui-ci.\n\n
Mais voilà qu'après plusieurs jours à galoper sans arrêt, vous décidez de vous arrêter dans la petite ville de LuckyLand.""")
        print("\n...\n...\n...\n")
        print("Ce petit hôtel fera très bien l'affaire pour me reposer")