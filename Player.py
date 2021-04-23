class Player:
    """
    Класс Player отвечает за игрока.
    """
    def __init__(self):
        """
        Определяются progress, coins, attack_damage, auto_attack_damage,
        coins_for_upgrade_attack и coins_for_upgrade_auto_attack для игрока.
        """
        self.progress = 0
        self.coins = 0
        self.attack_damage = 1
        self.auto_attack_damage = 0
        self.coins_for_upgrade_attack = 30
        self.coins_for_upgrade_auto_attack = 20
