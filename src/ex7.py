"""
En utilisant python (3.6 mini) et P5 :
    - Ouvrir une fenêtre de 500px par 500px.
    - Dessiner un carré rouge aux coordonnées aléatoires (avec la fonction random.randint(a,b))
    - Déplacer le carré rouge de façon aléatoire lorsque l'utilisateur clique dessus.
    - Afficher dans l'angle haut-gauche, le nombre de clics fait sur le carré rouge
"""

import core
import random

def setup() :
    core.fps = 30
    core.WINDOW_SIZE = [500, 500]

    core.memory("SQUARE_SIZE", 100)

    core.memory("squareX", random.randint(0, 500 - core.memory("SQUARE_SIZE")))
    core.memory("squareY", random.randint(0, 500 - core.memory("SQUARE_SIZE")))

    core.memory("RED", (255, 0, 0))
    core.memory("WHITE", (255, 255, 255))

    core.memory("CPT", 0)

def run() :
    
    if core.getMouseLeftClick():
        
        clicX, clicY = core.getMouseLeftClick()

        x = core.memory("squareX")
        y = core.memory("squareY")

        taille = core.memory("SQUARE_SIZE")

        if clicX >= x and clicX <= x + taille and clicY >= y and clicY <= y + taille :

            core.cleanScreen()

            core.memory("squareX", random.randint(0, 500 - core.memory("SQUARE_SIZE")))
            core.memory("squareY", random.randint(0, 500 - core.memory("SQUARE_SIZE")))

            core.memory("CPT", core.memory("CPT") + 1)

    # Dessiner le carré
    core.Draw.rect(core.memory("RED"), (core.memory("squareX"), core.memory("squareY"), core.memory("SQUARE_SIZE"), core.memory("SQUARE_SIZE")))

    # Ecrire le texte sur la fenetre 
    core.Draw.text(core.memory("WHITE"), str(core.memory("CPT")), (30, 15), 60)

core.main(setup, run)

