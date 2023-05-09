import character
import tkinter as tk
import tkinter.ttk as ttk

# main loop/logic
def main():

    pl = character(True,1,"John")
    en = character(False,1,"Wolf")

    def lvl():
        pl.level_up()
        i = pl.get_level()
        player_lvl2["text"] = f"{i}"

    #Window setup
    window = tk.Tk(className="Fighter")
    window.columnconfigure([0,1,2],minsize=250,uniform=True)

    #Player Card setup
    player_frame = tk.Frame(master=window,relief="raised",width=200,height=100)
    player_frame.grid(sticky="nsew",row=0,column=0)

    #player name
    player_namel = tk.Label(master=player_frame,text="Name: ")
    player_namel.grid(row=0,column=0)
    player_name = tk.Label(master=player_frame,text=pl.get_name())
    player_name.grid(row=0,column=1)
    #player LVL
    player_lvl1 = tk.Label(master=player_frame,text="LVL: ")
    player_lvl1.grid(row=1,column=0)
    player_lvl2 = tk.Label(master=player_frame,text=pl.get_level())
    player_lvl2.grid(row=1,column=2)
    player_lvl3 = tk.Button(master=player_frame,text="+",command=lvl)
    player_lvl3.grid(row=1,column=3)
    #player EXP


    #Actions panel Setup
    mid_frame = tk.Frame(master=window,relief="flat",width=100,background="black")
    mid_frame.grid(sticky="nsew",row=0,column=1)

    #Enemy Card Setup
    enemy_frame = tk.Frame(master=window,relief="raised",width=200)
    enemy_frame.grid(sticky="nsew",row=0,column=2)


    window.mainloop()
   


main()