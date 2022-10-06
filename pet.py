import random
from screeninfo import get_monitors
import tkinter as tk

window = tk.Tk()
import_path = "animations/"
state = 0 #determines which behaviour
pos_x = 100

#[all animations]
idle = [tk.PhotoImage(file=import_path+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
idle_to_sleep = [tk.PhotoImage(file=import_path+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
sleep = [tk.PhotoImage(file=import_path+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
sleep_to_idle = [tk.PhotoImage(file=import_path+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file=import_path+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
walk_negative = [tk.PhotoImage(file=import_path+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif

animations = {
    "idle":{
        "animation":idle,
        "spd":100
        },
    "idle_to_sleep":{
        "animation":idle_to_sleep,
        "spd":200
    },
    "sleep":{
        "animation":sleep,
        "spd":1000
    }
}

cycle = 0
current_animation = "idle"
animation_spd = animations.get(current_animation).get("spd")
move_spd = 1
frame = animations.get(current_animation).get("animation")[0] #current frame of the animation

def update_geometry(x = 100,y = 540):
    # print("update geometry")
    window.geometry('100x100+'+str(x)+"+"+str(y))

def play_animation():
    global cycle
   # print(f"cycle: {cycle}")
    cycle += 1
    if cycle >= len(animations.get(current_animation).get("animation")): 
        cycle = 0
        
    frame = animations.get(current_animation).get("animation")[cycle]
    label.configure(image=frame)
    # print("animation")
    window.after(animation_spd, update)

def determine_state():
    """picks new state every run"""
    pass

def update():
    global pos_x
    global state
    
    match state:
        case 0:
            pos_x+= move_spd
            if pos_x > 1920:
                state = 1
        case 1:
            pos_x-= move_spd
            if pos_x < 0:
                state = 0
    
    update_geometry(pos_x)
    determine_state()
    window.after(1, play_animation)
    #window.after(1, update)

def mouseClick(event):
    print("mouse clicked")

#loop the program
window.after(1,update)

window.config(highlightbackground="black")
label = tk.Label(window,bd=0,bg='black')
window.geometry('100x100')
label = tk.Label(window,bd=0,bg='black')

label.configure(image=frame)
label.pack()

label.bind("<Button>",mouseClick)

window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

window.attributes("-topmost",True)
window.update()

window.mainloop()