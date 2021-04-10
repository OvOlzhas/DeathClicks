import random

from GameObject import GameObject
import GlobalVariables


class Enemy(GameObject):
    """
    Класс Enemy отвечает за всех врагов.
    Наследуется от GameObject.
    От этого класса наследуются типы врагов: Ogre, Goblin, Boss_Nikita, Griffin, Minotaur.
    """
    def __init__(self):
        """
        Создает врага.
        Определяются level и hp врага.
        """
        GameObject.__init__(self)
        # Рандомно враг может быть сильнее, чем ожидалось.
        self.level = GlobalVariables.player.progress + random.randint(0, 2)
        self.hp = GlobalVariables.MIN_HP + self.level * GlobalVariables.increase_HP
        self.timer_for_update = 8


# Для каждого юнита был создан свой класс, для дальнейших потенциальных изменений.


class Goblin(Enemy):
    """
    Наследуется от Enemy.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Goblin"
        self.image = GlobalVariables.goblin_png
        self.rect = self.image.get_rect()


class Boss_Nikita(Enemy):
    """
    Наследуется от Enemy.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "BOSS Nikita"
        self.image = GlobalVariables.nikita_png
        # У босса больше хп чем у обычных юнитов в 2.3 раза
        self.hp = int(self.hp * 2.3)
        self.rect = self.image.get_rect()


class Minotaur(Enemy):
    """
    Наследуется от Enemy.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Minotaur"
        self.image = GlobalVariables.minotaur_png
        self.rect = self.image.get_rect()


class Ogre(Enemy):
    """
    Наследуется от Enemy.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Ogre"
        self.image = GlobalVariables.ogre_png
        self.rect = self.image.get_rect()


class Griffin(Enemy):
    """
    Наследуется от Enemy.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Griffin"
        self.image = GlobalVariables.griffin_png
        self.rect = self.image.get_rect()
