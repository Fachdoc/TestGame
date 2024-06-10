from MonsterTemplates import *
from MonsterCreator import MonsterCreator
from Arena import Arena

class GameConsoleInterface:
    def __init__(self):
        mc = MonsterCreator()
        playerMonster = Monster
        arena = Arena

        while True:





            print("==============================================")
            print("Choose your path:")
            print("1. Create new lv1 Warrior")
            print("2. Enter Arena")
            print("3. Exit")
            value = input("Insert number: ")
            print("==============================================")

            match value:
                case '1':
                    playerMonster = mc.createMonster(1)
                    print(playerMonster)
                case '2':
                    arena = Arena(playerMonster)
                case '3':
                    break
                case _:
                    print("Wrong input, try again")