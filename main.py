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




    def receive_DMG(self,damage):
        self.HP -= damage
        pass
    def deal_DMG(self):
        return self.Attack_DMG
        pass
    def heal_HP(self,heal):
        self.HP += heal
    def print_character(self):
        print("Name: ",self.name,"\tLVL: ",self.LVL)
        print("HP:",self.HP,cl.Color.GREEN,"/",self.MAX_HP,cl.Color.OFF,"\tATK: ",self.Attack_DMG,"\n")
    def get_SPD(self):
        return self.SPD
    def isalive(self):
        if self.HP > 0 :
            return True
        else : return False
    


# main loop/logic
def main():
    pl = character()
    pl.print_character()
    return


main()