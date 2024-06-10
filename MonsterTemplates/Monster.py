from MonsterTemplates.MonsterType import MonsterType

class Monster:
    def __init__(self, name, health, attack, deffence, type):
        if not isinstance(name, str):
            raise TypeError("Wrong name Type")

        if not isinstance(health,int):
            raise TypeError("Wrong health type")

        if not isinstance(attack, int):
            raise TypeError("Wrong attack Type")

        if attack<0:
            raise ValueError("Attack less than 0")

        if not isinstance(deffence, int):
            raise TypeError("Wrong defence Type")
        if deffence<0:
            raise ValueError("Deffence less than 0")

        if not isinstance(type, MonsterType):
            raise TypeError("Wrong monster type Type")

        self.name = name
        self.health = health
        self.attack = attack
        self.deffence = deffence
        self.type = type
        self.initiative = 0


    def __str__(self):
        string = "=========================================\n"
        string += "Name: " + self.name + "\n"
        string += "Type: " + str(self.type.name) + "\n"
        string += "Health: " + str(self.health) + "\n"
        string += "Attack: " + str(self.attack) + "\n"
        string += "Deffence: " + str(self.deffence) + "\n"
        string += "========================================\n"

        return string

    def islAive(self):
        return self.health > 0

