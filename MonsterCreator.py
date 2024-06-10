from MonsterNames.EarthNames import EarthNames
from MonsterNames.LightNames import LightNames
from MonsterTemplates import *
from MonsterNames import *
import random

class MonsterCreator:

    def createMonster(self, value = 'R'):

        str = random.randint(1, 10)
        con = random.randint(1, 10)
        dex = random.randint(1, 10)
        per = random.randint(1, 10)
        intel = random.randint(1, 10)
        wis = random.randint(1, 10)

        lv = random.randint(1, 20)

        #type = MonsterType(1)
        type = MonsterType(random.randint(1, len(list(MonsterType))))

        match type:
            case MonsterType.HUMANOID:
                name = HumanoidNames(lv).name
            case MonsterType.UNDEAD:
                name = UndeadNames(lv).name
            case MonsterType.RADIANT:
                name = RadiantNames(lv).name
            case MonsterType.HELLISH:
                name = HellishNames(lv).name
            case MonsterType.VOID:
                name = VoidNames(lv).name
            case MonsterType.NATURE:
                name = NatureNames(lv).name
            case MonsterType.EARTH:
                name = EarthNames(lv).name
            case MonsterType.WATER:
                name = WaterNames(lv).name
            case MonsterType.FIRE:
                name = FireNames(lv).name
            case MonsterType.LIGHT:
                name = LightNames(lv).name
            case MonsterType.DARK:
                name = DarkNames(lv).name

        name = name.replace('_', ' ').replace('PP', "'")

        if isinstance(value, int) and value > 0 and value < 7:
            return Monster(name, value, str, con, dex, per, intel, wis, type)

        return Monster(name, (lv//4) + 1, str, con, dex, per, intel, wis, type)
