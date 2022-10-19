import random
from sre_parse import State
import tkinter as tk

class pet:
    window = tk.Tk()
    init_state = "idle"
    state = init_state
    current_animation = 0
    animation_frames = 0
    animation_cycle = 0
    animation_spd = 100
    UPDATE_SPD = 1
    animation_repetition = 1
    cycle = 0
    repetition = 0
    frame = [tk.PhotoImage(file="animations/idle.gif",format = 'gif -index %i' %(i)) for i in range(5)][0]
    label = tk.Label(window,bd=0,bg='black')


    states_data = {}
    

    def __init__(self) -> None:
        pass

    def add_state(self, state_name, animation, behaviour, animation_spd = 100, repetition = 1):
        self.states_data[state_name] = {
            "animation":animation,
            "animation_spd":animation_spd,
            "repetition":repetition,
            "behaviour":behaviour
        }


    def set_state(self, new_state):

        self.state = new_state
        self.animation_spd = self.states_data.get(new_state).get('animation_spd')
        self.animation_repetition = self.states_data.get(new_state).get('repetition')
        self.animation_frames = len(self.states_data.get(new_state).get('animation'))
        self.cycle = 0
        self.animation_cycle = 0
        self.repetition = 0
    
        print(f'enter state ',new_state)
    
    def choose_random_state(self):
        return random.choice(list(self.states_data.keys())) 
        # self.set_state(new_state)

    pick_state = choose_random_state
    """holds the function that changes the state"""

    def play_animation(self):
        self.animation_cycle += 1
        # self.cycle+=1
        # print(self.animation_cycle)
        if self.animation_cycle >= self.animation_spd:
            self.cycle += 1
            self.animation_cycle = 0
        
        if self.cycle == self.animation_frames: 
            self.cycle = 0
            self.repetition += 1
            
        frame = self.states_data.get(self.state).get('animation')[self.cycle] # frame = animations.get(current_animation).get("animation")[cycle]
        # print(frame)
        self.label.configure(image=frame)
        # print("animation")
        self.window.after(self.UPDATE_SPD, self.update)

    def update(self):
        self.states_data.get(self.state).get("behaviour")()
        if self.repetition >= self.animation_repetition: self.set_state(self.pick_state())
        
        self.window.after(self.UPDATE_SPD, self.play_animation)

    def mouseClick(self, event):
        print("meow")
    MouseClickEvent = mouseClick


    def start(self):
        """animal appears in the init state"""
        print('start pet')
        self.cycle = 1
        self.window.after(1,self.update)

        self.window.config(highlightbackground="black")
        self.window.geometry('100x100+500+500')
        

        self.label.configure(image=self.frame)
        self.label.pack()

        self.label.bind("<Button>",self.MouseClickEvent)

        self.window.overrideredirect(True)
        self.window.wm_attributes('-transparentcolor','black')

        self.window.attributes("-topmost",True)
        self.window.update()

        self.window.mainloop()

def idle_state():
    # print('idle state')
    pass

def get_animation_spd_seconds(pet : pet, time_in_miliseconds):
    return time_in_miliseconds / pet.UPDATE_SPD

if __name__ == "__main__":
    cat = pet()
    idle_animation = [tk.PhotoImage(file="animations/idle.gif",format = 'gif -index %i' %(i)) for i in range(5)]
    cat.add_state('idle', animation=idle_animation, behaviour= idle_state, animation_spd=100, repetition=20)
    cat.set_state('idle')
    cat.start()