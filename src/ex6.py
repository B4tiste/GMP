"""
    En utilisant python (3.6 mini) et P5 :
        - Ouvrir une fenêtre de 500px par 500px
        - Dessiner un rond blanc de 100px centré en 250x250
        - Assombrir le rond a chaque fois que l'utilisateur appuie sur la touche « n »
        - Eclaircir le rond a chaque fois que l'utilisateur appuie sur la touche « b »
    /!\ Attention les couleurs ne peuvent être comprises qu'entre O et 255.
"""

import core

def setup():
    core.fps = 30
    core.WINDOW_SIZE = [500, 500]

    core.memory("R", 255)
    core.memory("G", 255)
    core.memory("B", 255)

    core.memory("circleX", 250)
    core.memory("circleY", 250)

    core.memory("CIRCLE_SIZE", 100)

def run():

    if core.getKeyPressList("n") and core.memory("R") > 0:

        core.memory("R", core.memory("R") - 5)
        core.memory("G", core.memory("G") - 5)
        core.memory("B", core.memory("B") - 5)

    elif core.getKeyPressList("b") and core.memory("R") < 255:
        
        core.memory("R", core.memory("R") + 5)
        core.memory("G", core.memory("G") + 5)
        core.memory("B", core.memory("B") + 5)
    
    # Dessiner le cercle
    core.Draw.circle((core.memory("R"), core.memory("G"), core.memory("B")), (core.memory("circleX"), core.memory("circleY")), core.memory("CIRCLE_SIZE"))

core.main(setup, run)