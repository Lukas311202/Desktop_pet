from random import random
import pet
import tkinter as tk
import random

def idle_state():
    # print("idle state")
    pass
def determine_state():
    print('determine state')
    return 'idle'

def hiss(event):
    print('hiss') if random.randint(0,1) == 0 else print('meow')

cat = pet.pet()
cat.pick_state = determine_state
cat.MouseClickEvent = hiss
idle_animation = [tk.PhotoImage(file="animations/idle.gif",format = 'gif -index %i' %(i)) for i in range(5)]
cat.add_state('idle', animation=idle_animation, behaviour= idle_state, animation_spd=pet.get_animation_spd_seconds(cat,170), repetition=10)
cat.set_state('idle')
cat.start()