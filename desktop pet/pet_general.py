import random
import ctypes
import move_window
import tkinter as tk

window = tk.Tk()
import_path = "animations/"
state = 2 #determines which behaviour
#idle state
#sleep state
#move state
#wake up state
user32 = ctypes.windll.user32
start_pos_y = [800]
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f"width {screen_width}")
window_title = "Editor"
pos_x = int(screen_width * 0.85)
pet_size = 100
task_bar_size = 40
pos_y = screen_height - task_bar_size - pet_size
window_pos = [screen_width, 100]

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
        "spd":100,
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
    },
    "drag_window":{
        "animation":idle,
        "spd":300,
        'repetition':10
    }
}

repetition = 0
cycle = 0
animation_cycle = 0
current_animation = "idle"
animation_spd = animations.get(current_animation).get("spd")
UPDATE_SPD = 5
move_spd = 1
frame = animations.get(current_animation).get("animation")[0] #current frame of the animation

def update_geometry(x = 500,y = 600):
    # print("update geometry")
    window.geometry(str(pet_size)+'x'+str(pet_size)+"+"+str(x)+"+"+str(y))

def play_animation():
    global animation_cycle
    global cycle
    global repetition
   # print(f"cycle: {cycle}")
    animation_cycle += 1
    if animation_cycle >= animation_spd:
        cycle += 1
        animation_cycle = 0
    
    if cycle >= len(animations.get(current_animation).get("animation")): 
        cycle = 0
        repetition += 1
        
    frame = animations.get(current_animation).get("animation")[cycle]
    label.configure(image=frame)
    # print("animation")
    window.after(UPDATE_SPD, update)

def set_state(new_state):
    global state
    global current_animation
    global animation_spd
    global cycle
    global repetition
    global window_pos

    if new_state == state:
        return
    state = new_state
    state_str = ""
    match state:
        case 0:
            state_str = 'idle'
        case 1:
            state_str = 'sleep'
        case 2:
            state_str = 'drag_window'
            # window_pos = [screen_width, 100]
            
        
    current_animation = state_str
    animation_spd = animations.get(current_animation).get('spd')
    cycle = 0
    repetition = 0
    
    print(f'enter state ',state_str)
    
def determine_state():
    """picks new state every run"""
    new_state = random.randint(0,2)
    set_state(new_state)

def update():
    global pos_x
    global pos_y
    global state
    global window_pos
    
    match state:
        case 0:
            #pos_x+= move_spd
            if pos_x > 1920:
                state = 1
        case 1:
            #pos_x-= move_spd
            if pos_x < 0:
                state = 0
        case 2:
            #drag window
            if move_window.window_exists(window_title):

                pos_x = move_window.get_window_position(window_title).left - 100
                pos_y = move_window.get_window_position(window_title).top + 100

                window_pos[0] -= 5
                move_window.move_window(window_title, window_pos)
            else:
                print(f'window with title {window_title} does not exist')
                set_state(0)

    
    update_geometry(pos_x, pos_y)
    if repetition >= animations.get(current_animation).get('repetition'): determine_state()
    window.after(UPDATE_SPD, play_animation)
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
