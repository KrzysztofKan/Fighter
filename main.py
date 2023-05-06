import colorist as cl

# setup base variables for balance
base_Hp = 10
base_DMG = 1
base_Strenght = 1
base_Dexterity = 1
base_Armor = 0
# stats multipliers
base_HP_per_Strenght = 5
base_DMG_per_Strenght = 2
base_SPD_per_Dexterity = 2


# character class defining basic attributes and functions
class character():
    def __init__(self,player = False) -> None:
        self.LVL = 1
        self.name = 'Joe'
        self.MAX_HP = base_Hp + (base_Strenght * base_HP_per_Strenght)
        self.HP = self.MAX_HP
        self.Attack_DMG = base_Strenght * base_DMG_per_Strenght
        self.SPD = base_Dexterity
        self.alive = True




    def receive_DMG():
        pass
    def deal_DMG():
        pass
    def heal_HP():
        pass
    def print_character(self):
        print("Name: ",self.name,"\tLVL: ",self.LVL)
        print("HP:",self.HP,"/",self.MAX_HP,"\tATK: ",self.Attack_DMG,"\n")
        pass
    def get_SPD():
        pass
    def isalive():
        pass







# main loop/logic
def main():
    pl = character()
    pl.print_character()
    return


main()