# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random


class Fighter:

    def __init__(self, hp=0, strength=0, magic=0, defense=0, evasion=0):
        self.hp = hp * 10
        self.strength = strength * 2
        self.magic = magic * 5
        self.defense = defense
        self.evasion = evasion * .7


class Barbarian(Fighter):
    attacks = ["Sword Thrust", "Mega Kick", "The Rock Bottom"]

    def __init__(self):
        super(Barbarian, self).__init__(10, 8, 2, 7, 3)


class Mage(Fighter):
    attacks = ["Fire Ball", "Lightning Shock", "Icicle Launch"]

    def __init__(self):
        super(Mage, self).__init__(9, 1, 10, 7, 3)


class Archer(Fighter):
    attacks = ["Super Arrow", "Pocket Sand", "Shadow Arrow"]

    def __init__(self):
        super(Archer, self).__init__(7, 3, 3, 3, 10)


def start_battle(player, competitor):
    print("You are battling a " + competitor.__class__.__name__)
    print(player)
    while player.hp > 0 or competitor.hp > 0:
        print(f"{player.hp} vs {competitor.hp}")

        attack = 0
        while True:
            try:
                for idx, attack in enumerate(player.attacks):
                    print(f"{idx + 1}: {attack}")
                attack = int(input("Please choose an attack"))
                if attack > 3 or attack < 1:
                    raise ValueError()
                break
            except ValueError:
                print("Please choose a valid number")

        competitor.hp -= battle(player, attack, random.randint(1, 3))

        while True:
            try:
                for i in range(1, 4):
                    print(f"Press {i} to block attackers {i} attack")
                defense = int(input("Please choose an defense"))
                if defense > 3 or defense < 1:
                    raise ValueError()
                break
            except ValueError:
                print("Please choose a valid number")

        player.hp -= battle(competitor, random.randint(1, 3), defense)
    if player.hp < 0:
        print("You got Rekted")
    else:
        print("You won")


def battle(attacker, attack, defense):
    if attack == defense:
        print(attacker.__class__.__name__ + "missed!")
        return 0
    else:
        return attacker.strength


def main():
    player = Archer()
    competitor = Barbarian()
    while True:
        print('''
            1: Barbarian - Strong and high health
            2: Mage - High mag attack but it needs to charge
            3: Archer - Hard to hit sneaky guy
        ''')

        try:
            player_class = int(input("Please choose a class"))
            if player_class > 3 or player_class < 1:
                raise ValueError()
            break
        except ValueError:
            print("Please choose a valid number")
        if player_class == 1:
            player = Barbarian()
        elif player_class == 2:
            player = Mage()
        elif player_class == 3:
            player = Archer()
        else:
            print("Theres a bug")
            exit(0)
    start_battle(player, competitor)


if __name__ == '__main__':
    main()


