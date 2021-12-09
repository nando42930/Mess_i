from abc import ABCMeta, abstractmethod

# Parent class of Tank, Artillery, Infantry and Robot.
class Player(metaclass=ABCMeta):

    # Player constructor.
    def __init__(self, strength, attacks, health):
        self.strength = strength
        self.attacks = attacks
        self.health = health

    # Each child class has its own impact, mutable along the game.
    @property
    @abstractmethod
    def attack_impact(self):
        pass

    # Updates attacks remaining, after an attack.
    def has_attacked(self):
        self.attacks -= 1

    # Checks if the given instance has died, after an attack.
    def is_dead(self):
        return self.health <= 0


# Child class of Player.
class Tank(Player):

    # Tank constructor.
    def __init__(self):
        super().__init__(200, 2, 200)

    # Implements abstract method, which is also a property of the object.
    @property
    def attack_impact(self):
        return int(self.strength * self.health / 200)


# Child class of Player.
class Artillery(Player):

    # Artillery constructor.
    def __init__(self):
        super().__init__(500, 1, 50)

    # Implements abstract method, which is also a property of the object.
    @property
    def attack_impact(self):
        return int(self.strength * self.health / 50)


# Child class of Player.
class Infantry(Player):

    # Infantry constructor.
    def __init__(self):
        super().__init__(100, 3, 100)

    # Implements abstract method, which is also a property of the object.
    @property
    def attack_impact(self):
        return int(self.strength * self.health / 100)


# Child class of Player.
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

    # Robot constructor.
    def __init__(self):
        super().__init__(None, None, 750)
        self.nrg = 500

    # Implemented to assure inheritance.
    @property
    def attack_impact(self):
        pass

    # Recovers 50% of his nrg in the beginning of each turn till a MAX of 500.
    def heal(self):
        self.nrg = 500 if self.nrg * 1.5 > 500 else int(self.nrg * 1.5)

    # Heals Robot depending on which type of healing is done, if it has enough nrg.
    def heal_type(self, type):
        if type == 1 and self.nrg >= 200:
            self.health += Robot.HEAL1
            self.nrg -= Robot.HEAL1_NRG
        elif type == 2 and self.nrg >= 300:
            self.health += Robot.HEAL2
            self.nrg -= Robot.HEAL2_NRG
        elif type == 3 and self.nrg >= 400:
            self.health += Robot.HEAL3
            self.nrg -= Robot.HEAL3_NRG
        else:
            print("Not enough energy to heal.")
            return False
        return True

    # Attacks a certain target by crane, touch or sound.
    def attack(self, type, target):
        if type == 1 and self.nrg >= Robot.CRANE_NRG:
            self.nrg -= Robot.CRANE_NRG
            target.health -= Robot.CRANE
        elif type == 2 and self.nrg >= Robot.TOUCH_NRG:
            self.nrg -= Robot.TOUCH_NRG
            target.health -= Robot.TOUCH
        elif type == 3 and self.nrg >= Robot.SOUND_NRG:
            self.nrg -= Robot.SOUND_NRG
            target.health -= Robot.SOUND
        else:
            print("Not enough energy to attack.")
            return False
        return True



""" """ """ """ """ """ """ TESTING SECTION """ """ """ """ """ """ """

# print()
# print("######################## TESTING ########################")
# print()
# robot_1 = Robot()
# print("Strength:", robot_1.strength, " Attacks:", robot_1.attacks, end = "  ")
# print("Health:", robot_1.health, end = "  ")
# print("Attack impact:", robot_1.attack_impact, " Energy:", robot_1.nrg)
# robot_1.heal_type(2)
# print("Health:", robot_1.health, " Energy:", robot_1.nrg)
# robot_1.heal_type(3)
# robot_1.heal()
# print("Health:", robot_1.health, " Energy:", robot_1.nrg)
# print()
# inf_1 = Infantry()
# print("Strength:", inf_1.strength, " Attacks:", inf_1.attacks, end = "  ")
# print("Health:", inf_1.health, " Attack impact:", inf_1.attack_impact)
# inf_1.has_attacked()
# print("Infantry attacked once. Attacks remaining:", inf_1.attacks)
# robot_1.attack(3, inf_1)
# print("Infantry was attacked. Health remaining:", inf_1.health, end = "  ")
# print("Current attack impact:", inf_1.attack_impact)
# robot_1.attack(1, inf_1)
# print()