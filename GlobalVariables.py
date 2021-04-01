import pygame
from Player import Player
from Enemies import Goblin
import os

# Constants
WIDTH = 811
HEIGHT = 980
FPS = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MIN_HP = 20

ENEMY_POSITION = (200, 400)

ENEMIES = ('Goblin', 'Nikita', 'Griffin', 'Minotaur', 'Ogre')

# Player initialization
player = Player()

# Paths
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Images')
sound_folder = os.path.join(game_folder, 'Sounds')

# Images of enemy
background = pygame.image.load(os.path.join(img_folder, 'Forest_background.jpeg'))
goblin_png = pygame.image.load(os.path.join(img_folder, 'Goblin.png'))
nikita_png = pygame.image.load(os.path.join(img_folder, 'Nikita.png'))
griffin_png = pygame.image.load(os.path.join(img_folder, 'Griffin.png'))
minotaur_png = pygame.image.load(os.path.join(img_folder, 'Minotaur.png'))
ogre_png = pygame.image.load(os.path.join(img_folder, 'Ogre.png'))

# Game initialization
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death clicks")

# Sounds for game
pygame.mixer.music.load(os.path.join(sound_folder, 'background_music.wav'))
attack_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'attack_sound.wav'))
nikita_sound = (pygame.mixer.Sound(os.path.join(sound_folder, 'Nikita_sound.wav')),
                pygame.mixer.Sound(os.path.join(sound_folder, 'Nikita_sound_2.wav')))

# First enemy initialization
enemy = Goblin()
enemy.hp = 10
