from abc import ABCMeta

class Enemy(metaclass=ABCMeta):

    attack_impact = None

    def __init__(self, strength, attacks, health):
        self.strenght = None
        self.attacks = None
        self.health = None

    def has_attacked(self):
        self.attacks -= 1

    def was_attacked(self, health):
        self.health -= health

    @abstractmethod
    def calc_impact(self):


class Tank(Enemy):

    def __init__(self):
        super().strength = 200
        super().attacks = 2
        super().health = 200

    def calc_impact(self):
        self.attack_impact = strength * health / 200


class Artillery(Enemy):

    def __init__(self):
        super().strength = 500
        super().attacks = 1
        super().health = 50

    def calc_impact(self):
        self.attack_impact = strength * health / 50


class Infantry(Enemy):

    def __init__(self):
        super().strength = 100
        super().attacks = 3
        super().health = 100

    def calc_impact(self):
        self.attack_impact = strength * health / 100