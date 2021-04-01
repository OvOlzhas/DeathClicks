import GlobalVariables
import random
from GameObject import GameObject


class Enemy(GameObject):
    """
    Класс Enemy отвечает за всех врагов.
    Наследуется от GameObject.
    От этого класса наследуются типы врагов: Ogre, Goblin, Nikita, Griffin, Minotaur.
    В классе определена функция __init__.
    """
    def __init__(self):
        """
        Создает врага.
        Определяются level и hp врага.
        """
        GameObject.__init__(self)
        self.level = max(1, GlobalVariables.player.progress + random.randint(0, 2))
        self.hp = GlobalVariables.MIN_HP + self.level * 10
        self.name = 'None'
        self.timer_for_update = 8


class Goblin(Enemy):
    """
    Класс Goblin отвечает тип врага - Goblin.
    Наследуется от Enemy.
    В классе определена функция __init__.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Goblin"
        self.image = GlobalVariables.goblin_png
        self.rect = self.image.get_rect()


class Nikita(Enemy):
    """
    Класс Nikita отвечает тип врага - Nikita.
    Наследуется от Enemy.
    В классе определена функция __init__.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Nikita"
        self.image = GlobalVariables.nikita_png
        self.rect = self.image.get_rect()


class Minotaur(Enemy):
    """
    Класс Minotaur отвечает тип врага - Minotaur.
    Наследуется от Enemy.
    В классе определена функция __init__.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Minotaur"
        self.image = GlobalVariables.minotaur_png
        self.rect = self.image.get_rect()


class Ogre(Enemy):
    """
    Класс Ogre отвечает тип врага - Ogre.
    Наследуется от Enemy.
    В классе определена функция __init__.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Ogre"
        self.image = GlobalVariables.ogre_png
        self.rect = self.image.get_rect()


class Griffin(Enemy):
    """
    Класс Griffin отвечает тип врага - Griffin.
    Наследуется от Enemy.
    В классе определена функция __init__.
    """
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Griffin"
        self.image = GlobalVariables.griffin_png
        self.rect = self.image.get_rect()
