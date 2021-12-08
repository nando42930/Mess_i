from abc import ABCMeta, abstractmethod

class Enemy(metaclass=ABCMeta):

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

    def was_attacked(self, health):
        self.health -= health


class Tank(Enemy):

    def __init__(self):
        super().__init__(200, 2, 200)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 200)


class Artillery(Enemy):

    def __init__(self):
        super().__init__(500, 1, 50)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 50)


class Infantry(Enemy):

    def __init__(self):
        super().__init__(100, 3, 100)

    @property
    def attack_impact(self):
        return int(self.strength * self.health / 100)


print()
print("######################## TESTING ########################")
print()
inf_1 = Infantry()
print("Strength:", inf_1.strength, " Attacks:", inf_1.attacks, end = "  ")
print("Health:", inf_1.health, " Attack impact:", inf_1.attack_impact)
inf_1.has_attacked()
print("Infantry attacked once. Attacks remaining:", inf_1.attacks)
inf_1.was_attacked(10)
print("Infantry was attacked. Health remaining:", inf_1.health, end = "  ")
print("Current attack impact:", inf_1.attack_impact)
print()