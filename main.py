import pygame

from Draw_functions import draw_enemy, update_enemy_position
from Gamefunctions import input_processing, print_all_text, auto_attack, check_enemy
import GlobalVariables


def game():
    """
    Запуск игры, обработка входных данных и вывод дисплея.
    """
    clock = pygame.time.Clock()

    # Циклический вывод фонового звука
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    # Названия говорят сами за себя
    timer_for_auto_attack = GlobalVariables.FPS

    while input_processing():
        # Вывод фона
        GlobalVariables.display.blit(GlobalVariables.background, (0, 0))

        # Вывод всего нужного текста
        print_all_text()

        # Отрисовка врага
        update_enemy_position()
        draw_enemy()

        # Вывод отрисованного
        pygame.display.flip()

        # Отслеживание за FPS
        clock.tick(GlobalVariables.FPS)

        # Авто-Атака
        if timer_for_auto_attack == 0:
            auto_attack()
            check_enemy()
            timer_for_auto_attack = GlobalVariables.FPS
        timer_for_auto_attack -= 1

    # Закрытие игры
    pygame.quit()


game()
