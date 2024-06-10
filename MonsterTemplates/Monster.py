from MonsterTemplates.MonsterType import MonsterType

class Monster:
    def __init__(self, name, lv, str, con, dex, per, intel, wis, type):

        #stats for creation
        self.name = name
        self.type = type

        self.level= lv

        self.strenght = str  * (1+lv/5)
        self.constitution = con  * (1+lv/5)
        self.dexterity = dex  * (1+lv/5)
        self.perception = per  * (1+lv/5)
        self.intelligence = intel  * (1+lv/5)
        self.wisdom = wis  * (1+lv/5)

        #race base stats
        #stats calculated
        self.health = int(100*(1+((self.constitution+self.wisdom)/10)))

        self.strAttack = int(10*(1+(self.strenght*self.dexterity/20)))
        self.intAttack = int(10*(1+(self.intelligence*self.dexterity/20)))

        self.strDefense = int(10*(1+(self.constitution/10)))
        self.intDefense = int(10*(1+(self.wisdom)/10))


        self.initiative = 0




    def __str__(self):
        string = "=========================================\n"
        string += "Name: " + self.name + "\n"
        string += "Level: " + str(self.level) + "\n"
        string += "Type: " + str(self.type.name) + "\n"
        string += "Health: " + str(self.health) + "\n"
        string += "Strength Attack: " + str(self.strAttack) + "\n"
        string += "Magick Attack: " + str(self.intAttack) + "\n"
        string += "Strength Deffence: " + str(self.strDefense) + "\n"
        string += "Magick Deffence: " + str(self.intDefense) + "\n"
        string += "========================================\n"

        return string

    def islAive(self):
        return self.health > 0
