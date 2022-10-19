"""
    Space invaders game
"""

import core
import random

# Player class
class Entity():
    def __init__(self, category: str, x: int, y: int, color: str, speed: int, hp: int, size: int = 20):
        self.category = category
        self.x = x
        self.y = y
        self.color = colors[color]
        self.speed = speed
        self.hp = hp
        self.size = size                

# Data
CIRCLE_TRESHOLD = 10

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "cyan": (0, 255, 255),
}

tbl_colors = [color for color in colors if color != "white"]
print(tbl_colors)

def setup():
    # Window parameter init
    core.fps = 60
    core.WINDOW_SIZE = [500, 700]
    core.setTitle("By B4tiste")

    # Player
    core.memory("PLAYER", Entity("player", core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2, "white", 5, 3, 15))
    core.memory("OPPONENTS", [])

    # Data
    core.memory("SCORE", 0)
    core.memory("LIFE", 3)
    core.memory("CPT", 0)
    core.memory("GAME_OVER", False)
    core.memory("TARGET_COLOR", colors[random.choice(tbl_colors)])

def player_control(entity):

    # Manage the player's movements
    # Vertical
    # UP
    if core.getKeyPressList("z") and entity.y >= (0 + entity.size + CIRCLE_TRESHOLD):
        entity.y -= entity.speed
    # DOWN
    elif core.getKeyPressList("s") and entity.y <= (core.WINDOW_SIZE[1] - entity.size - CIRCLE_TRESHOLD):
        entity.y += entity.speed
    
    # Horizontal
    # LEFT
    elif core.getKeyPressList("q") and entity.x >= (0 + entity.size + CIRCLE_TRESHOLD):
        entity.x -= entity.speed
    # RIGHT
    elif core.getKeyPressList("d") and entity.x <= (core.WINDOW_SIZE[0] - entity.size - CIRCLE_TRESHOLD):
        entity.x += entity.speed

def opponents_control(opponents):
    if opponents != []:
        for opponent in opponents:
            core.Draw.circle(opponent.color, (opponent.x, opponent.y), opponent.size)
            opponent.y += opponent.speed

            if opponent.y < 0 or opponent.y > core.WINDOW_SIZE[1]:
                opponents.remove(opponent)

# Function to check if two rectangles are colliding
def collision(a, b):
    return a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]

# Function to check if the player is colliding with an opponent
def collisions(player, opponents, target_color):
    if opponents != []:
        for opponent in opponents:
            opponent_hitbox =  (opponent.x - opponent.size, opponent.y - opponent.size, opponent.x + opponent.size, opponent.y + opponent.size)
            player_hitbox = (player.x - player.size, player.y - player.size, player.x + player.size, player.y + player.size)

            if collision(opponent_hitbox, player_hitbox):
                if opponent.color == target_color:
                    core.memory("SCORE", core.memory("SCORE") + 1)
                    core.memory("TARGET_COLOR", colors[random.choice(tbl_colors)])
                else:
                    core.memory("LIFE", core.memory("LIFE") - 1)

                opponents.remove(opponent)

                if core.memory("LIFE") == 0:
                    core.memory("GAME_OVER", True)

def run():
    # Clear the screen
    core.cleanScreen()

    # Game over
    if core.memory("GAME_OVER"):
        core.Draw.text(colors["red"], "Game Over", (0, 0), 50)
    else :
        # Data gathering
        player = core.memory("PLAYER")
        opponents = core.memory("OPPONENTS")
        score = core.memory("SCORE")
        life_count = core.memory("LIFE")
        target_color = core.memory("TARGET_COLOR")

        # Create a new oppent with random position and speed
        if random.randint(0, 10) == 1 and len(opponents) < 15:
            speed = random.randint(-5, 5)
            if speed == 0:
                speed = 1
            
            if speed > 0:
                opponents.append(Entity("opponent", random.randint(0, core.WINDOW_SIZE[0]), 0, random.choice(tbl_colors), speed, 1))
            else:
                opponents.append(Entity("opponent", random.randint(0, core.WINDOW_SIZE[0]), core.WINDOW_SIZE[1], random.choice(tbl_colors), speed, 1))

        # Draw each entity
        # Draw the player on the window
        core.Draw.circle(player.color, (player.x, player.y), player.size)

        # All function to handle the game behaviour
        # Check player control
        player_control(player)
        opponents_control(opponents)
        collisions(player, opponents, target_color)

        # Score :
        core.Draw.text(colors["white"], "Score : " + str(score), (10, 10), 40)

        # Life :
        core.Draw.text(colors["white"], "HP : " + str(life_count), (10, 50), 40)

        # Indicate the target color inside the player
        core.Draw.circle(target_color, (player.x, player.y), player.size*0.8)
        
# Run the app
core.main(setup, run)