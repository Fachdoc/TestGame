from MonsterTemplates.MonsterType import MonsterType
import random

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
        self.maxHealth = self.health

        self.strAttack = int(10*(1+(self.strenght*self.dexterity/20)))
        self.intAttack = int(10*(1+(self.intelligence*self.dexterity/20)))

        self.strDefense = int(10*(1+(self.constitution/10)))
        self.intDefense = int(10*(1+(self.wisdom)/10))

        #aditional stats
        self.initiative = self.dexterity
        self.experience = 0



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

    def isAlive(self):
        return  self.health >= 0

    def rest(self):
        self.health = self.maxHealth

    def heal(self, value):
        if self.health + value > self.maxHealth:
            self.health = self.maxHealth
        else:
            self.health += value
    def takePhysicalDamage(self, damage):
        if damage - self.strDefense >=0:
            self.health -= (damage - self.strDefense)

    def takeMagicalDamage(self, damage):
        if damage - self.intDefense:
            self.health -= (damage - self.intDefense)

    def rollInitiative(self):
        return random.randint(1,20) + self.initiative

    def physicalAttack(self):
        return self.strAttack
    def magicalAttack(self):
        return self.intAttack
    def attackTypeSelector(self):
        if self.physicalAttack()>=self.magicalAttack():
            return "physical"
        else:
            return "magical"
    def autoAttack(self, type):
        match type:
            case "physical":
                return self.physicalAttack()
            case "magical":
                return self.magicalAttack()
            case _:
                return self.physicalAttack()

    def autoDefense(self, type, damage):
        match type:
            case "physical":
                self.takePhysicalDamage(damage)
            case "magical":
                self.takeMagicalDamage(damage)
            case _:
                self.takePhysicalDamage(damage)

    def returnDamageTaken(self, damage, type):
        match type:
            case "physical":
                return damage - self.strDefens
            case "magical":
                return damage - self.intDefense
            case _:
                return damage - self.strDefens

    def returnTakenPhysicalDamage(self, damage):
        return damage-self.strDefense

    def returnTakenMagicalDamage(self, damage):
        return damage-self.intDefense

    def levelUp(self):
        if self.experience >= self.level*1000:
            self.level +=1
            print("LEVEL UP, now level is ", self.level)

    def addXP(self, value):
        self.experience += value

    def returnDefence(self, type):
        match type:
            case "physical":
                return self.strDefense
            case "magical":
                return self.intDefense
            case _:
                return self.strDefense