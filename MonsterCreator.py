from MonsterNames.EarthNames import EarthNames
from MonsterNames.LightNames import LightNames
from MonsterTemplates import *
from MonsterNames import *
import random

class MonsterCreator:

    def createMonster(self):
        health = random.randint(50, 100)
        attack = random.randint(15, 30)
        deffense = random.randint(0, 15)
        #type = MonsterType(11)
        type = MonsterType(random.randint(1, len(list(MonsterType))))

        match type:
            case MonsterType.HUMANOID:
                name = HumanoidNames(random.randint(1, len(list(HumanoidNames)))).name.replace('_', ' ')
            case MonsterType.UNDEAD:
                name = UndeadNames(random.randint(1, len(list(UndeadNames)))).name.replace('_', ' ')
            case MonsterType.RADIANT:
                name = RadiantNames(random.randint(1, len(list(RadiantNames)))).name.replace('_', ' ')
            case MonsterType.HELLISH:
                name = HellishNames(random.randint(1, len(list(HellishNames)))).name.replace('_', ' ')
            case MonsterType.VOID:
                name = VoidNames(random.randint(1, len(list(VoidNames)))).name.replace('_', ' ')
            case MonsterType.NATURE:
                name = NatureNames(random.randint(1, len(list(NatureNames)))).name.replace('_', ' ')
            case MonsterType.EARTH:
                name = EarthNames(random.randint(1, len(list(EarthNames)))).name.replace('_',' ')
            case MonsterType.WATER:
                name = WaterNames(random.randint(1, len(list(WaterNames)))).name.replace('_', ' ').replace('PP', "'")
            case MonsterType.FIRE:
                name = FireNames(random.randint(1, len(list(FireNames)))).name.replace('_', ' ')
            case MonsterType.LIGHT:
                name = LightNames(random.randint(1, len(list(LightNames)))).name.replace('_', ' ')
            case MonsterType.DARK:
                name = DarkNames(random.randint(1, len(list(DarkNames)))).name.replace('_', ' ')
        return Monster(name, health, attack, deffense, type)