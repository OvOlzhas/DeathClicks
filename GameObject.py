import collections
import pygame

import GlobalVariables

XY_pos = collections.namedtuple("XY_pos", "x y")


class GameObject(pygame.sprite.Sprite):
    """
    Класс GameObject отвечает за игровые объекты.
    Наследуется от pygame.sprite.Sprite для возможности отрисовки.
    """
    def __init__(self):
        """
        Запускается pygame.sprite.Sprite.__init__, а также определяется позиция объекта.
        Так как у нас сейчас только Enemy, задается фиксированная начальная позиция Enemy.
        """
        pygame.sprite.Sprite.__init__(self)
        self.position = XY_pos(GlobalVariables.ENEMY_POSITION[0], GlobalVariables.ENEMY_POSITION[1])
