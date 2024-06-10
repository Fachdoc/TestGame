from MonsterNames import *
from MonsterTemplates import *
from MonsterCreator import MonsterCreator
from Arena import Arena
import random


if __name__ == '__main__':

    mc = MonsterCreator()

    for i in range(2):
        print(mc.createMonster())


    #arena = Arena(zombie1,zombie2)
    #arena.fight()



