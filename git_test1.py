class Equipment:

    def __init__(self, name, strong, protection):
        self.name = name
        self.strong = strong
        self.protection = protection


class Hero:
    def __init__(self, name, rang: int, health, strong, equipment: list):
        self.name = name
        self.rang = rang
        self.health = health
        self.strong = strong
        self.equipment = equipment

    def fight(self, other_hero):
        if 0 < self.rang <= 3 and 0 < other_hero.rang <= 3 and 0 < self.strong <= 100:
            other_hero.health = other_hero.health - (self.strong * self.rang)

        if self.health < 0:
            print(f'{self.name} is dead')

    def health_recovery(self):
        if 0 < self.health < 100:
            self.health = self.health + 3

    def get_rang(self):
        if 0 < self.rang <= 3:
            return self.rang

    def set_rang(self, value):
        if 0 < value <= 3:
            self.__rang = value

    def get_health(self):
        if 0 < self.health <= 100:
            return self.health

    def set_health(self, value):
        if 0 < value <= 100:
            self.__health = value

    def get_equipment(self):
        return self.equipment

    def set_equipment(self, value):
        self.__equipment = self.equipment.append(value)

    rang = property(get_rang, set_rang)

    health = property(get_health, set_health)

    equipment = property(get_equipment, set_equipment)


shield = Equipment(name='shield', strong=0, protection=7)
sword = Equipment(name='sword', strong=7, protection=3)
armor = Equipment(name='armor', strong=0, protection=5)

victor = Hero(name='victor', rang=1, health=70, strong=5, equipment=[shield])
artur = Hero(name='artur', rang=3, health=100, strong=10, equipment=[sword])
maks = Hero(name='maks', rang=2, health=80, strong=7, equipment=[armor])
