import gameGrid6
import random 

current_state = "s1"
q_table = {
  "up": [0,0,0,0,0,0],
  "down": [0,0,0,0,0,0],
  "right": [0,0,0,0,0,0],
  "left": [0,0,0,0,0,0],
}


learning_rate = 0.1
actions= ["up", "down", "right", "left"]

def transitions(state, action):
    next_state = state
    if (state == "s0" and action == "down") :
        next_state= "s4"
    elif (state == "s1" and action == "down") :
        next_state= "s3"
    elif (state == "s1" and action == "up") :
        next_state= "s5"
    elif (state == "s2" and action == "left") :
        next_state= "s3"
    elif (state == "s3" and action == "left") :
        next_state= "s4"
    elif (state == "s3" and action == "up") :
        next_state= "s1"
    elif (state == "s3" and action == "right") :
        next_state= "s2"
    elif (state == "s4" and action == "down") :
        next_state= "s5"
    elif (state == "s4" and action == "right") :
       next_state= "s3"
    elif (state == "s4" and action == "up") :
       next_state= "s0"

    return next_state
