import pygame
import random

import GlobalVariables


def mouse_command(click_position):
    """
    Обрабатывает клик в зависимости от позиции.
    :param click_position: Координаты места, где произошел клик
    """
    if GlobalVariables.enemy.rect.collidepoint(click_position):
        # Удар прошелся по врагу
        GlobalVariables.player.coins += GlobalVariables.player.attack_damage
        GlobalVariables.enemy.hp -= GlobalVariables.player.attack_damage
        # Вызов звука после удара
        if GlobalVariables.enemy.name != "BOSS Nikita":
            pygame.mixer.Sound.play(GlobalVariables.attack_sound)
        else:
            pygame.mixer.Sound.play(GlobalVariables.nikita_sound[random.randint(0, 1)])
    # Проверка того, была ли нажата та область, где находится кнопка UPGRADE,
    # которая находиться рядом с Your Damage
    upgade_botton_x = [GlobalVariables.WIDTH - GlobalVariables.upgrade_width
                       - GlobalVariables.distance_from_the_sides,
                       GlobalVariables.WIDTH]
    upgade_botton_y = [GlobalVariables.distance_between_pos_texts * 1 + GlobalVariables.distance_from_the_sides,
                       GlobalVariables.distance_between_pos_texts * 1 + GlobalVariables.distance_from_the_sides
                       + GlobalVariables.text_height]
    if upgade_botton_y[0] <= click_position[1] <= upgade_botton_y[1] and \
            upgade_botton_x[0] <= click_position[0] <= upgade_botton_x[1] and \
            GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_attack:
        # Была нажата кнопка UPGRADE у Your Damage
        # Улучшение урона за клик
        GlobalVariables.player.attack_damage += 1
        GlobalVariables.player.coins -= GlobalVariables.player.coins_for_upgrade_attack
        GlobalVariables.player.coins_for_upgrade_attack = \
            int(GlobalVariables.player.coins_for_upgrade_attack * GlobalVariables.price_increase_factor)
    # Проверка того, была ли нажата та область, где находится кнопка UPGRADE,
    # которая находиться рядом с Your AutoAttackDamage
    upgade_auto_botton_x = [GlobalVariables.WIDTH - GlobalVariables.upgrade_width
                            - GlobalVariables.distance_from_the_sides,
                            GlobalVariables.WIDTH]
    upgade_auto_botton_y = [GlobalVariables.distance_between_pos_texts * 2 + GlobalVariables.distance_from_the_sides,
                            GlobalVariables.distance_between_pos_texts * 2 + GlobalVariables.distance_from_the_sides
                            + GlobalVariables.text_height]
    if upgade_auto_botton_y[0] <= click_position[1] <= upgade_auto_botton_y[1] and \
            upgade_auto_botton_x[0] <= click_position[0] <= upgade_auto_botton_x[1] and \
            GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_auto_attack:
        # Была нажата кнопка UPGRADE у Your AutoAttackDamage
        # Улучшение урона за Авто-атаку
        GlobalVariables.player.auto_attack_damage += 1
        GlobalVariables.player.coins -= GlobalVariables.player.coins_for_upgrade_auto_attack
        GlobalVariables.player.coins_for_upgrade_auto_attack = \
            int(GlobalVariables.player.coins_for_upgrade_auto_attack * GlobalVariables.price_increase_factor)


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
    for enemy in GlobalVariables.ENEMIES:
        if GlobalVariables.enemy.name != enemy:
            enemies_without_enemy.append(enemy)
    enemy_name = enemies_without_enemy[random.randint(0, len(GlobalVariables.ENEMIES) - 2)]
    if GlobalVariables.player.progress % GlobalVariables.boss_rarity == 0:
        enemy_name = 'BOSS Nikita'
        pygame.mixer.Sound.play(GlobalVariables.nikita_laugh)
    GlobalVariables.enemy = GlobalVariables.ENEMY_CREATE[enemy_name]()


def auto_attack():
    """
    Воспроизводиться Авто-атака по врагу
    Дается в три раза меньше монет за каждый урон.
    """
    GlobalVariables.enemy.hp -= GlobalVariables.player.auto_attack_damage
    GlobalVariables.player.coins += GlobalVariables.player.auto_attack_damage // 3


def print_text(message, x, y, font_color=GlobalVariables.standard_text_color,
               font_type=GlobalVariables.default_font, font_size=GlobalVariables.text_height):
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


def print_all_text():
    """
    Вывод текста
    """
    # Левый верхний угол соседних строк находятся на расстоянии distance_between_pos_texts
    # Поэтому появляются коэффициенты перед distance_between_pos_texts
    print_text(f'Coins: {GlobalVariables.player.coins}',
               GlobalVariables.distance_from_the_sides,
               GlobalVariables.distance_from_the_sides)
    print_text(f'Your Damage: {GlobalVariables.player.attack_damage}',
               GlobalVariables.distance_from_the_sides,
               GlobalVariables.distance_between_pos_texts * 1 + GlobalVariables.distance_from_the_sides)
    if GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_attack:
        print_text('UPGRADE',
                   GlobalVariables.WIDTH - GlobalVariables.upgrade_width - GlobalVariables.distance_from_the_sides,
                   GlobalVariables.distance_between_pos_texts * 1 + GlobalVariables.distance_from_the_sides)
    print_text(f'Your AutoAttackDamage: {GlobalVariables.player.auto_attack_damage}',
               GlobalVariables.distance_from_the_sides,
               GlobalVariables.distance_between_pos_texts * 2 + GlobalVariables.distance_from_the_sides)
    if GlobalVariables.player.coins >= GlobalVariables.player.coins_for_upgrade_auto_attack:
        print_text('UPGRADE',
                   GlobalVariables.WIDTH - GlobalVariables.upgrade_width - GlobalVariables.distance_from_the_sides,
                   GlobalVariables.distance_between_pos_texts * 2 + GlobalVariables.distance_from_the_sides)

    print_text(f'{GlobalVariables.enemy.name} level: {GlobalVariables.enemy.level}',
               GlobalVariables.distance_from_the_sides,
               GlobalVariables.distance_between_pos_texts * 3 + GlobalVariables.distance_from_the_sides)
    print_text(f'{GlobalVariables.enemy.name} HP: {GlobalVariables.enemy.hp}',
               GlobalVariables.distance_from_the_sides,
               GlobalVariables.distance_between_pos_texts * 4 + GlobalVariables.distance_from_the_sides)

    if GlobalVariables.player.progress % GlobalVariables.boss_rarity == 0 and GlobalVariables.player.progress != 0:
        # У надписи BOSS FIGHT свой цвет (230, 20, 20), а также размер 100
        print_text('BOSS FIGHT', GlobalVariables.WIDTH - GlobalVariables.boss_fight_width,
                   GlobalVariables.distance_between_pos_texts * 3 + GlobalVariables.distance_from_the_sides,
                   font_size=100, font_color=(230, 20, 20))


def input_processing() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Нажата кнопка закрытия программы
            return False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Нажата ЛКМ
            mouse_command(event.pos)
        check_enemy()
    return True
