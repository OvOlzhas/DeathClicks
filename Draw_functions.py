import random

import GlobalVariables


def update_enemy_position():
    """
    Случайное перемещение врага по дисплею.
    """
    if GlobalVariables.enemy.timer_for_update == 0:
        random_dist = 50
        boundaries = [-200, 300]
        GlobalVariables.enemy.rect.x += random.randint(-random_dist, random_dist)
        GlobalVariables.enemy.rect.x = max(min(GlobalVariables.enemy.rect.x,
                                               GlobalVariables.ENEMY_POSITION[0] + boundaries[1]),
                                           GlobalVariables.ENEMY_POSITION[0] + boundaries[0])
        GlobalVariables.enemy.rect.y += random.randint(-random_dist, random_dist)
        GlobalVariables.enemy.rect.y = max(min(GlobalVariables.enemy.rect.y,
                                               GlobalVariables.ENEMY_POSITION[1] + boundaries[1]),
                                           GlobalVariables.ENEMY_POSITION[1] + boundaries[0])
        GlobalVariables.enemy.timer_for_update = 10
    GlobalVariables.enemy.timer_for_update -= 1


def draw_enemy():
    """
    Вывод врага на дисплей.
    """
    GlobalVariables.display.blit(GlobalVariables.enemy.image,
                                 (GlobalVariables.enemy.rect.x,
                                  GlobalVariables.enemy.rect.y))
