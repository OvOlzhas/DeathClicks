import GlobalVariables
import random


def update_enemy_position():
    """
    Случайное перемещение врага по дисплею.
    """
    if GlobalVariables.enemy.timer_for_update == 0:
        GlobalVariables.enemy.rect.x += random.randint(-50, 50)
        GlobalVariables.enemy.rect.x = max(min(GlobalVariables.enemy.rect.x,
                                               GlobalVariables.ENEMY_POSITION[0] + 300),
                                           GlobalVariables.ENEMY_POSITION[0] - 200)
        GlobalVariables.enemy.rect.y += random.randint(-50, 50)
        GlobalVariables.enemy.rect.y = max(min(GlobalVariables.enemy.rect.y,
                                               GlobalVariables.ENEMY_POSITION[1] + 300),
                                           GlobalVariables.ENEMY_POSITION[1] - 200)
        GlobalVariables.enemy.timer_for_update = 10
    GlobalVariables.enemy.timer_for_update -= 1


def draw_enemy():
    """
    Вывод врага на дисплей.
    """
    GlobalVariables.display.blit(GlobalVariables.enemy.image,
                                 (GlobalVariables.enemy.rect.x,
                                  GlobalVariables.enemy.rect.y))
