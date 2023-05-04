import colorist as cl

# setup variables for balance
base_Hp = 10
base_DMG = 1
base_Strenght = 1
base_Dexterity = 1
base_Armor = 0

base_HP_per_Strenght = 5
base_DMG_per_Strenght = 2


# character class defining basik attributes and functions
class character():
    def __init__(self,player = False) -> None:
        if player == False:
            self.MAX_HP = base_Hp + (base_Strenght * base_HP_per_Strenght)
            self.HP = self.MAX_HP
            self.Attack_DMG = base_Strenght * base_DMG_per_Strenght
        else:
            self.MAX_HP = base_Hp + (base_Strenght * base_HP_per_Strenght)
            self.HP = self.MAX_HP
            self.Attack_DMG = base_Strenght * base_DMG_per_Strenght

    

    def receive_DMG():
        pass
    def deal_DMG():
        pass
    def heal_HP():
        pass
    def print_character():
        pass
    def isalive():
        pass







# main loop/logic
def main():
    return


main()