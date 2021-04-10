import os
import pygame

from Enemies import Goblin, Griffin, Ogre, Minotaur, Boss_Nikita
from Player import Player

# Constants
WIDTH = 811
HEIGHT = 980
FPS = 150

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MIN_HP = 20

ENEMY_POSITION = (200, 400)

distance_from_the_sides = 10
distance_between_texts = 5
text_height = 50
distance_between_pos_texts = distance_between_texts + text_height
upgrade_width = 150
boss_fight_width = 400

boss_rarity = 8

price_increase_factor = 1.5
increase_HP = 10

standard_text_color = (255, 70, 50)

ENEMIES = ('Goblin', 'Griffin', 'Minotaur', 'Ogre')
ENEMY_CREATE = {'Goblin': Goblin,
                'Griffin': Griffin,
                'Minotaur': Minotaur,
                'Ogre': Ogre,
                'BOSS Nikita': Boss_Nikita}

# Player initialization
player = Player()

# Paths
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Images')
sound_folder = os.path.join(game_folder, 'Sounds')
font_folder = os.path.join(game_folder, 'Fonts')

# Images of enemy
background = pygame.image.load(os.path.join(img_folder, 'Forest_background.jpeg'))
goblin_png = pygame.image.load(os.path.join(img_folder, 'Goblin.png'))
nikita_png = pygame.image.load(os.path.join(img_folder, 'Nikita.png'))
griffin_png = pygame.image.load(os.path.join(img_folder, 'Griffin.png'))
minotaur_png = pygame.image.load(os.path.join(img_folder, 'Minotaur.png'))
ogre_png = pygame.image.load(os.path.join(img_folder, 'Ogre.png'))

# Fonts
default_font = os.path.join(font_folder, 'Konstanting_font.ttf')

# Game initialization
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death clicks")

# Sounds for game
pygame.mixer.music.load(os.path.join(sound_folder, 'background_music.wav'))
attack_sound = pygame.mixer.Sound(os.path.join(sound_folder, 'attack_sound.wav'))
attack_sound.set_volume(0.3)
nikita_sound = (pygame.mixer.Sound(os.path.join(sound_folder, 'Nikita_sound.wav')),
                pygame.mixer.Sound(os.path.join(sound_folder, 'Nikita_sound_2.wav')))
nikita_sound[0].set_volume(0.5)
nikita_sound[1].set_volume(0.5)
nikita_laugh = pygame.mixer.Sound(os.path.join(sound_folder, 'Laugh_of_Nikita.wav'))

# First enemy initialization
enemy = Goblin()
enemy.hp = 10
