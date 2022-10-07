import random
from screeninfo import get_monitors
import tkinter as tk

window = tk.Tk()
import_path = "animations/"
state = 0 #determines which behaviour
#idle state
#sleep state
#move state
#wake up state
start_pos_y = [800]
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
print(f"width {screen_width}")
pos_x = int(screen_width * 0.85)
pet_size = 100
task_bar_size = 40
pos_y = screen_height - task_bar_size - pet_size

#[all animations]
idle = [tk.PhotoImage(file=import_path+'idle.gif',format = 'gif -index %i' %(i)) for i in range(5)]#idle gif
idle_to_sleep = [tk.PhotoImage(file=import_path+'idle_to_sleep.gif',format = 'gif -index %i' %(i)) for i in range(8)]#idle to sleep gif
sleep = [tk.PhotoImage(file=import_path+'sleep.gif',format = 'gif -index %i' %(i)) for i in range(3)]#sleep gif
sleep_to_idle = [tk.PhotoImage(file=import_path+'sleep_to_idle.gif',format = 'gif -index %i' %(i)) for i in range(8)]#sleep to idle gif
walk_positive = [tk.PhotoImage(file=import_path+'walking_positive.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to left gif
walk_negative = [tk.PhotoImage(file=import_path+'walking_negative.gif',format = 'gif -index %i' %(i)) for i in range(8)]#walk to right gif
#kitty_sandwich = [tk.PhotoImage(file=import_path+'kitty_sandwich.gif',format = 'gif -index %i' %(i)) for i in range(15)]

animations = {
    "idle":{
        "animation":idle,
        "spd":200,
        'repetition':20
        },
    "idle_to_sleep":{
        "animation":idle_to_sleep,
        "spd":200
    },
    "sleep":{
        "animation":sleep,
        "spd":800,
        'repetition':5
    }
}

repetition = 0
cycle = 0
current_animation = "idle"
animation_spd = animations.get(current_animation).get("spd")
move_spd = 1
frame = animations.get(current_animation).get("animation")[0] #current frame of the animation

def update_geometry(x = 500,y = 600):
    # print("update geometry")
    window.geometry(str(pet_size)+'x'+str(pet_size)+"+"+str(x)+"+"+str(y))

def play_animation():
    global cycle
    global repetition
   # print(f"cycle: {cycle}")
    cycle += 1
    if cycle >= len(animations.get(current_animation).get("animation")): 
        cycle = 0
        repetition += 1
        
    frame = animations.get(current_animation).get("animation")[cycle]
    label.configure(image=frame)
    # print("animation")
    window.after(animation_spd, update)

def set_state(new_state):
    global state
    global current_animation
    global animation_spd
    global cycle
    global repetition
    if new_state == state:
        return
    state = new_state
    state_str = ""
    match state:
        case 0:
            state_str = 'idle'
        case 1:
            state_str = 'sleep'
        
    current_animation = state_str
    animation_spd = animations.get(current_animation).get('spd')
    cycle = 0
    repetition = 0
    
    print(f'enter state ',state_str)
    
def determine_state():
    """picks new state every run"""
    new_state = random.randint(0,1)
    set_state(new_state)

def update():
    global pos_x
    global state
    
    match state:
        case 0:
            #pos_x+= move_spd
            if pos_x > 1920:
                state = 1
        case 1:
            #pos_x-= move_spd
            if pos_x < 0:
                state = 0
    
    update_geometry(pos_x, pos_y)
    if repetition >= animations.get(current_animation).get('repetition'): determine_state()
    window.after(1, play_animation)
    #window.after(1, update)

def mouseClick(event):
    print("meow")

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
