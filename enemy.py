class Enemy:

    def __init__(self, strength, attacks, health):


class Tank(Enemy):

    def __init__(self):
        super().strength = 200
        super().attacks = 2
        super().health = 200


class Artillery(Enemy):

    def __init__(self):
        super().strength = 500
        super().attacks = 1
        super().health = 50


class Infantry(Enemy):

    def __init__(self):
        super().strength = 100
        super().attacks = 3
        super().health = 100