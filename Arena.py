from MonsterTemplates.Monster import Monster
from MonsterCreator import MonsterCreator


class Arena:

    def __init__(self, monster1):
        self.monster1 = monster1
        self.arenaConsoleInterface()

    def arenaConsoleInterface(self):
        while True:
            print("==============================================")
            print("What you wanna do in Arena:")
            print("1. Fight monster")
            print("2. Exit")
            value = input("What is your choice?: ")

            match value:
                case '1':
                    self.fightConsoleInterface()
                case '2':
                    break
                case _:
                    print("Invalid imput, try again")

    def fightConsoleInterface(self):
        while True:
            print("==============================================")
            print("Pick monster level:")
            print("Number between 1 and 6 ")
            print("Exit - to exit")
            value = input("What is your choice?: ")



            enemy = Monster

            match value:
                case 'Exit':
                    break
                case '1' | '2' | '3' | '4' | '5' | '6' :
                    mc = MonsterCreator()
                    enemy = mc.createMonster(int(value))
                    print(enemy)
                case _, "":
                    print("Invalid input try again")
            print("==============================================")
            self.fight(enemy)



    def fight(self, monster2):

        print("==============================================")
        print("Lets begin ")
        print("Roll the iniciative:")
        playerRoll = self.monster1.rollInitiative()
        print("Players roll: ",playerRoll)
        monsterRoll = monster2.rollInitiative()
        print("Monsters roll: ", monsterRoll)

        gladiatorsList = []

        if monsterRoll>=playerRoll:
            print("==============================================")
            print("Monster is first")
            print("==============================================")
            gladiatorsList.append(monster2)
            gladiatorsList.append(self.monster1)
        else:
            print("==============================================")
            print("Player is first")
            print("==============================================")
            gladiatorsList.append(self.monster1)
            gladiatorsList.append(monster2)

        counter = 0

        input("Press Enter to continue")

        while self.monster1.isAlive() & monster2.isAlive():
            print('\n','\n','\n','\n','\n','\n','\n','\n','\n','\n','\n')
            print("Round ", counter+1," ==============================================")
            damage = 0
            type = ''

            lastHp = gladiatorsList[(counter+1)%2].health

            if gladiatorsList[counter%2].name == self.monster1.name:
                print("Choose your attack:")
                print("1. physical(",self.monster1.physicalAttack(),")")
                print("2. magical(", self.monster1.magicalAttack(),")")

                match input("Give type: "):
                    case '1':
                        type = 'physical'
                        damage = gladiatorsList[counter%2].physicalAttack()
                    case '2':
                        type = 'magical'
                        damage = gladiatorsList[counter % 2].magicalAttack()


                gladiatorsList[(counter + 1) % 2].autoDefense(type, damage)


            else:
                damage = gladiatorsList[counter % 2].physicalAttack()
                gladiatorsList[(counter + 1) % 2].takePhysicalDamage(damage)

            print(gladiatorsList[counter%2].name, " hit ", gladiatorsList[(counter+1)%2].name, " with ", type , " damage")
            print("Player ","=========================")
            print(self.monster1.name)

            damageTaken = 0

            if gladiatorsList[(counter + 1)%2].name == self.monster1.name:
                damageTaken = damage - self.monster1.returnDefence(type)
                if damageTaken<0:
                    damageTaken = 0
                print(lastHp, "-", damageTaken, "(", damage, " - ", self.monster1.returnDefence(type), ") ->", self.monster1.health)
            else :
                print(self.monster1.health)

            print("Monster ", "=========================")
            print(monster2.name)
            if gladiatorsList[(counter + 1)%2].name == monster2.name:
                damageTaken = damage-monster2.returnDefence(type)
                if damageTaken<0:
                    damageTaken = 0
                print(lastHp, "-", damageTaken, "(", damage, " - ", monster2.returnDefence(type), ") ->", monster2.health)
            else :
                print(monster2.health)

            counter+=1

            print("=========================")
            input("Press Enter to continue...")

            if not self.monster1.isAlive():
                print("Player lost")
            if not monster2.isAlive():
                print("Monster lost")
                xp = (monster2.health + monster2.physicalAttack() + monster2.magicalAttack())*monster2.level
                print("Player get ", xp," xp")
                self.monster1.addXP(xp)
                print("Player XP: ", self.monster1.experience, "/", self.monster1.level * 1000)
                self.monster1.levelUp()