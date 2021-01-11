import random


class Fighter:

    def charge_special(self):
        self.attacks.append(self.special[0])

    def spend_special(self):
        self.attacks.pop()
        return self.special[1]

    def __init__(self, hp=0, strength=0, magic=0, defense=0, evasion=0):
        self.hp = hp * 10
        self.strength = strength * 2
        self.magic = magic * .5
        self.defense = defense
        self.evasion = evasion * .7


class Barbarian(Fighter):
    attacks = ["Sword Thrust", "Mega Kick", "The Rock Bottom"]
    special = "Round House Kick", 10
    def __init__(self):
        super(Barbarian, self).__init__(10, 8, 2, 7, 3)


class Mage(Fighter):
    attacks = ["Fire Ball", "Lightning Shock", "Icicle Launch"]
    special = "Expectro Petrona", 30
    def __init__(self):
        super(Mage, self).__init__(6, 4, 10, 7, 3)


class Archer(Fighter):
    attacks = ["Super Arrow", "Pocket Sand", "Shadow Arrow"]
    special = "Double Arrow", 20

    def __init__(self):
        super(Archer, self).__init__(7, 8, 5, 0, 10)


def start_battle(player, competitor):

    print("You are battling a " + competitor.__class__.__name__)
    while player.hp > 0 or competitor.hp > 0:
        if len(player.attacks) <= 3:
            player_special = random.randint(1, 10) < player.magic
        else:
            player_special = False

        competitor_special = random.randint(1, 10) < competitor.magic

        if player_special:
            player.charge_special()
        if competitor_special:
            competitor.charge_special()

        print(f"You: {player.hp}        Enemy: {competitor.hp}")

        attack = 0
        while True:
            try:
                for idx, attack in enumerate(player.attacks):
                    print(f"{idx + 1}: {attack}")
                attack = int(input("Please choose an attack\n"))
                if attack > len(player.attacks) or attack < 1:
                    raise ValueError()
                break
            except ValueError:
                print("Please choose a valid number")

        competitor.hp -= battle(player, attack, competitor, random.randint(1, 3))
        print(f"You: {player.hp}        Enemy: {competitor.hp}")

        while True:
            if competitor.hp <= 0:
                break
            try:
                for i in range(1, 4):
                    print(f"Press {i} to block attackers {i} attack")
                defense = int(input("Please choose an defense\n"))
                if defense > len(competitor.attacks) or defense < 1:
                    raise ValueError()
                break
            except ValueError:
                print("Please choose a valid number")
        if competitor_special:
            player.hp -= battle(competitor, 4, player, defense)
        else:
            player.hp -= battle(competitor, random.randint(1, 3), player, defense)

        if player.hp <= 0:
            print("You got Rekted")
            break
        elif competitor.hp <= 0:
            print("You won")
            break


def battle(attacker, attack, defender, defense):

    if random.randint(1, 10) < defender.evasion:
        if attack == 4:
            print("Epic fail you missed your special")
        else:
            print(defender.__class__.__name__ + " evaded!")
        return 0

    if attack == 4:
        print(attacker.__class__.__name__ + " used special " + attacker.special[0])
        attacker.spend_special()
        return attacker.special[1]
    if attack == defense:
        print(attacker.__class__.__name__ + " was blocked!")
        return 0
    else:
        print(attacker.__class__.__name__ + " hit!")
        return attacker.strength - defender.defense


def assignClass(class_number):
    assigned_class = Fighter()
    if class_number == 1:
        assigned_class = Barbarian()
    elif class_number == 2:
        assigned_class = Mage()
    elif class_number == 3:
        assigned_class = Archer()
    else:
        print("Theres a bug")
        exit(0)
    return assigned_class


def main():
    player = None
    competitor = None
    competitor_input = random.randint(1, 3)
    player_input = 0
    while True:
        print('''
            1: Barbarian - Strong and high health
            2: Mage - High mag attack but it needs to charge
            3: Archer - Hard to hit sneaky guy
        ''')

        try:
            player_input = int(input("Please choose a class\n"))
            if player_input > 3 or player_input < 1:
                raise ValueError()
            break
        except ValueError:
            print("Please choose a valid number")
    player = assignClass(player_input)
    competitor = assignClass(competitor_input)

    start_battle(player, competitor)


if __name__ == '__main__':
    main()
