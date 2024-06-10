from MonsterTemplates.Monster import Monster
import random
class Arena:

    def __init__(self, monster1, monster2):
        self.monster1 = monster1
        self.monster2 = monster2


    def fight(self):
        if not isinstance(self.monster1, Monster) and not isinstance(self.monster2, Monster):
            return print("Its not a monster")
        #else:
            #print("Its a monster")
        self.monster1.initiative = random.randint(1, 20)
        self.monster2.initiative = random.randint(1, 20)

        print(self.monster1.initiative)
        print(self.monster2.initiative)

