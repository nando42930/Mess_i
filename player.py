from abc import ABCMeta, abstractmethod

class Player(metaclass=ABCMeta):

    def __init__(self, strength, attacks, health):
        self.strength = strength
        self.attacks = attacks
        self.health = health

    @property
    @abstractmethod
    def attack_impact(self):
        pass

    def has_attacked(self):
        self.attacks -= 1

    def is_dead(self):
        return self.health <= 0


class Tank(Player):

    def __init__(self):
        super().__init__(200, 2, 200)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 200)


class Artillery(Player):

    def __init__(self):
        super().__init__(500, 1, 50)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 50)


class Infantry(Player):

    def __init__(self):
        super().__init__(100, 3, 100)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 100)


class Robot(Player):

    # Different attacks.
    CRANE = 200
    CRANE_NRG = 300
    TOUCH = 100
    TOUCH_NRG = 150
    SOUND = 50
    SOUND_NRG = 50
    
    # Types of healing.
    HEAL1 = 100
    HEAL1_NRG = 200
    HEAL2 = 200
    HEAL2_NRG = 300
    HEAL3 = 400
    HEAL3_NRG = 400

    def __init__(self):
        super().__init__(None, None, 750)
        self.nrg = 500

    @property
    def attack_impact(self):
        pass

    def heal(self, x):
        if x == 1 and self.nrg >= 200:
            self.health += Robot.HEAL1
            self.nrg -= Robot.HEAL1_NRG
        elif x == 2 and self.nrg >= 300:
            self.health += Robot.HEAL2
            self.nrg -= Robot.HEAL2_NRG
        elif x == 3 and self.nrg >= 400:
            self.health += Robot.HEAL3
            self.nrg -= Robot.HEAL3_NRG
        else: print("Not enough energy.")

    def attack(self, type, target):
        self.nrg -= Robot.CRANE_NRG if type == 1 else Robot.TOUCH_NRG if type == 2 else Robot.SOUND_NRG
        target.health -= Robot.CRANE if type == 1 else Robot.TOUCH if type == 2 else Robot.SOUND


print()
print("######################## TESTING ########################")
print()
robot_1 = Robot()
print("Strength:", robot_1.strength, " Attacks:", robot_1.attacks, end = "  ")
print("Health:", robot_1.health, end = "  ")
print("Attack impact:", robot_1.attack_impact, " Energy:", robot_1.nrg)
robot_1.heal(1)
print("Health:", robot_1.health, " Energy:", robot_1.nrg)
robot_1.heal(3)
print("Health:", robot_1.health, " Energy:", robot_1.nrg)
print()
inf_1 = Infantry()
print("Strength:", inf_1.strength, " Attacks:", inf_1.attacks, end = "  ")
print("Health:", inf_1.health, " Attack impact:", inf_1.attack_impact)
inf_1.has_attacked()
print("Infantry attacked once. Attacks remaining:", inf_1.attacks)
robot_1.attack(3, inf_1)
print("Infantry was attacked. Health remaining:", inf_1.health, end = "  ")
print("Current attack impact:", inf_1.attack_impact)
print()