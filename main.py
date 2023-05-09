import character as ch
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk,Image

# main loop/logic
def main():

    pl = ch.character(True,1,"John")
    en = ch.character(False,1,"Wolf")

    def lvlup():
        pl.level_up()
        i = pl.get_level()
        player_lvl2["text"] = f"{i}"

    #Window setup
    window = tk.Tk(className="Fighter")
    window.columnconfigure([0,1,2],minsize=250,uniform=True)
    window.resizable(False,False)

    #Player Card setup
    player_frame = tk.Frame(master=window,relief="raised",width=200,height=100)
    player_frame.grid(sticky="nsew",row=0,column=0)

    #Player portrait
    #portrait = ImageTk.PhotoImage(Image.open("C:\Python\Fighter\Assets\Portrait_Placeholder.bmp"))
    image = Image.open("C:\Python\Fighter\Assets\Portrait_Placeholder.bmp")
    image = image.resize((100,100))
    portrait = ImageTk.PhotoImage(image)
    
    
    portrait_frame = tk.Frame(master=player_frame,width=1,height=1,relief="raised")
    player_portrait = tk.Label(master=portrait_frame,image=portrait,anchor="center",width=100,height=100,justify="right")
    player_portrait.grid(row=0,column=0)
    portrait_frame.grid(row=0,column=4,columnspan=2,rowspan=10)
    

    #player name
    player_namel = tk.Label(master=player_frame,text="Name: ")
    player_namel.grid(row=0,column=0)
    player_name = tk.Label(master=player_frame,text=pl.get_name())
    player_name.grid(row=0,column=1)
    #player LVL
    player_lvl1 = tk.Label(master=player_frame,text="LVL: ",justify="left")
    player_lvl1.grid(row=1,column=0)
    player_lvl2 = tk.Label(master=player_frame,text=pl.get_level(),justify="center")
    player_lvl2.grid(row=1,column=1)
    player_lvl3 = tk.Button(master=player_frame,text="LVL Up",command=lvlup,overrelief="ridge")
    player_lvl3.grid(row=1,column=2)
    #playerEXP
    player_XPBar = ttk.Progressbar(master=player_frame,maximum=4,mode="determinate",value=1)
    s = ttk.Style
    player_XPBar
    player_XPBar.grid(row=3,column=1,columnspan=3)
    player_XP = tk.Label(master=player_frame,text="XP")
    player_XP.grid(row=3,column=0)
    player_EXP = tk.Label(master=player_frame,text="0")
    player_EXP.grid(row=3,column=1)
    player_EXPsep= tk.Label(master=player_frame,text="/")
    player_EXPsep.grid(row=3,column=2)
    player_MEXP = tk.Label(master=player_frame,text="100")
    player_MEXP.grid(row=3,column=3)
    player_XPBar = ttk.Progressbar(master=player_frame,maximum=100,phase=50)
    player_XPBar.grid(row=3,column=1,columnspan=3)

    #Actions panel Setup
    mid_frame = tk.Frame(master=window,relief="flat",width=100,background="black")
    mid_frame.grid(sticky="nsew",row=0,column=1)

    #Enemy Card Setup
    enemy_frame = tk.Frame(master=window,relief="raised",width=200)
    enemy_frame.grid(sticky="nsew",row=0,column=2)

    #player name
    enemy_namel = tk.Label(master=enemy_frame,text="Name: ")
    enemy_namel.grid(row=0,column=0)
    enemy_name = tk.Label(master=enemy_frame,text=en.get_name())
    enemy_name.grid(row=0,column=1)

    ver = tk.Label(master=window,text="Unversioned-Alpha",justify="right")
    ver.grid(row=1,column=2)

    window.mainloop()
   


main()