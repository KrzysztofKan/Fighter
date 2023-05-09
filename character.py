import colorist as cl
# setup base variables for balance
base_Hp = 10
base_DMG = 1
base_Strenght = 5
base_Dexterity = 5
base_Inteligence = 5
base_Armor = 0
# stats multipliers
str_HP_Mult = 22
str_HPreg_Mult = 0.1
agi_SPD_Mult = 1
agi_Armor_Mult = 0.167
int_Mana_Mult = 12
int_ManaReg_Mult = 0.05
int_MagRes_Mult = 0.1

base_DMG_per_Strenght = 2


# character class defining basic attributes and functions
class character():
    def __init__(self,player = False,LVL = 1,name = "") -> None:
        self.LVL = LVL
        self.name = name
        self.MAX_HP = base_Hp + (base_Strenght * str_HP_Mult)
        self.HP = self.MAX_HP
        self.Attack_DMG = base_Strenght * base_DMG_per_Strenght
        self.SPD = base_Dexterity * agi_SPD_Mult
        self.Armor = base_Armor + (base_Dexterity * agi_Armor_Mult)
        self.alive = True

    def receive_DMG(self,damage):
        self.HP -= damage
        pass

    def deal_DMG(self):
        return self.Attack_DMG

    def heal_HP(self,heal):
        self.HP += heal

    def get_level(self):
        return self.LVL
    
    def level_up(self):
        self.LVL +=1
    
    def get_name(self):
        return self.name

    def print_character(self):
        print("Name: ",self.name,"\tLVL: ",self.LVL)
        print("HP:",self.HP,cl.Color.GREEN,"/",self.MAX_HP,cl.Color.OFF,"\tATK: ",self.Attack_DMG,"\n")

    def get_SPD(self):
        return self.SPD
    
    def isalive(self):
        if self.HP > 0 :
            return True
        else : return False
    
