import pygame
from Player import Player
from Enemies import Goblin

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

# Images of enemy
background = pygame.image.load('Forest_background.jpeg')
goblin_png = pygame.image.load('Goblin.png')
nikita_png = pygame.image.load('Nikita.png')
griffin_png = pygame.image.load('Griffin.png')
minotaur_png = pygame.image.load('Minotaur.png')
ogre_png = pygame.image.load('Ogre.png')

# Game initialization
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death clicks")

# Sounds for game
pygame.mixer.music.load('background_music.wav')
attack_sound = pygame.mixer.Sound('attack_sound.wav')
nikita_sound = (pygame.mixer.Sound('Nikita_sound.wav'), pygame.mixer.Sound('Nikita_sound_2.wav'))

# First enemy initialization
enemy = Goblin()
enemy.hp = 10
