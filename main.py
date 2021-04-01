import pygame
import GlobalVariables
import random
from Enemies import Goblin, Minotaur, Nikita, Griffin, Ogre
from Draw_functions import draw_enemy, update_enemy_position


def mouse_command(click_position):
    """
    Обрабатывает клик в завсимости от позиции.
    :param click_position: Координаты места, где произошел клик
    """
    if GlobalVariables.enemy.rect.collidepoint(click_position):
        # Удар прошелся по врагу
        GlobalVariables.player.coins += GlobalVariables.player.attack_damage
        GlobalVariables.enemy.hp -= GlobalVariables.player.attack_damage
        if GlobalVariables.enemy.name != "Nikita":
            pygame.mixer.Sound.play(GlobalVariables.attack_sound)
        else:
            pygame.mixer.Sound.play(GlobalVariables.nikita_sound[random.randint(0, 1)])
    if 55 * 1 + 10 <= click_position[1] <= 55 * 1 + 60 and \
        GlobalVariables.WIDTH - 160 <= click_position[0] and \
            GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_attack:
        # Была нажата кнопка UPGRADE у Your Damage
        # Улучшение урона за клик
        GlobalVariables.player.attack_damage += 1
        GlobalVariables.player.coins -= GlobalVariables.player.coins_for_upgrade_attack
        GlobalVariables.player.coins_for_upgrade_attack = \
            int(GlobalVariables.player.coins_for_upgrade_attack * 1.5)
    if 55 * 2 + 10 <= click_position[1] <= 55 * 2 + 60 and \
        GlobalVariables.WIDTH - 160 <= click_position[0] and \
            GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_auto_attack:
        # Была нажата кнопка UPGRADE у Your AutoAttackDamage
        # Улучшение урона за Авто-атаку
        GlobalVariables.player.auto_attack_damage += 1
        GlobalVariables.player.coins -= GlobalVariables.player.coins_for_upgrade_auto_attack
        GlobalVariables.player.coins_for_upgrade_auto_attack = \
            int(GlobalVariables.player.coins_for_upgrade_auto_attack * 1.5)


def check_enemy():
    """
    Проверка на смерть врага.
    Если враг умер, создает новый через вызов new_enemy()
    """
    if GlobalVariables.enemy.hp <= 0:
        new_enemy()


def new_enemy():
    """
    Создает случайного нового врага, который не совпадает с нынешним.
    """
    GlobalVariables.player.progress += 1
    enemies_without_enemy = []
    for i in GlobalVariables.ENEMIES:
        if GlobalVariables.enemy.name != i:
            enemies_without_enemy.append(i)
    enemy_name = enemies_without_enemy[random.randint(0, 3)]
    if enemy_name == "Goblin":
        GlobalVariables.enemy = Goblin()
    if enemy_name == "Nikita":
        GlobalVariables.enemy = Nikita()
    if enemy_name == "Griffin":
        GlobalVariables.enemy = Griffin()
    if enemy_name == "Ogre":
        GlobalVariables.enemy = Ogre()
    if enemy_name == "Minotaur":
        GlobalVariables.enemy = Minotaur()


def auto_attack():
    """
    Возпроизводиться Авто-атака по врагу
    Дается в три раза меньше коинов за каждый урон.
    """
    GlobalVariables.enemy.hp -= GlobalVariables.player.auto_attack_damage
    GlobalVariables.player.coins += GlobalVariables.player.auto_attack_damage // 3


def print_text(message, x, y, font_color=(255, 70, 50),
               font_type='Konstanting_font.ttf', font_size=50):
    """
    Выводит текст в заданном цвете, позиции, шрифте и размере.
    :param message: Выводимый текст
    :param x: Позиция текста по х
    :param y: Позиция текста по у
    :param font_color: Цвет текста, который изначально равен (255, 70, 50)
    :param font_type: Шрифт текста, который изначально равен Konstanting_font.ttf
    :param font_size: Размер шрифта
    """
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    GlobalVariables.display.blit(text, (x, y))


def game():
    """
    Запуск игры, обработка входных данных и вывод дисплея.
    """
    clock = pygame.time.Clock()
    pygame.mixer.music.play(-1)

    timer_for_auto_attack = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Нажата кнопка закрытия программы
                running = False
                break
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # Нажата ЛКМ
                mouse_command(event.pos)
            check_enemy()
        # Вывод фона
        GlobalVariables.display.blit(GlobalVariables.background, (0, 0))

        # Вывод текста
        print_text(f'Coins: {GlobalVariables.player.coins}', 10, 10)
        print_text(f'Your Damage: {GlobalVariables.player.attack_damage}', 10, 55 * 1 + 10)
        if GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_attack:
            print_text(f'UPGRADE', GlobalVariables.WIDTH - 160, 55 * 1 + 10)
        print_text(f'Your AutoAttackDamage: {GlobalVariables.player.auto_attack_damage}', 10, 55 * 2 + 10)
        if GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_auto_attack:
            print_text(f'UPGRADE', GlobalVariables.WIDTH - 160, 55 * 2 + 10)

        print_text(f'{GlobalVariables.enemy.name} level: {GlobalVariables.enemy.level}', 10, 55 * 3 + 10)
        print_text(f'{GlobalVariables.enemy.name} HP: {GlobalVariables.enemy.hp}', 10, 55 * 4 + 10)

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
