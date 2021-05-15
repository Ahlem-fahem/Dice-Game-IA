import random
import game


epsilon = 0.1
learning_rate = 0.1
gamma = 0.9

MATRIX = {
  0: [0,0,0,0,0,0,0,0,0,0],
  1: [0,0,0,0,0,0,0,0,0,0],
  2: [0,0,0,0,0,0,0,0,0,0],
  3: [0,0,0,0,0,0,0,0,0,0],
  4: [0,0,0,0,0,0,0,0,0,0],
  5: [0,0,0,0,0,0,0,0,0,0],
  6: [0,0,0,0,0,0,0,0,0,0],
  7: [0,0,0,0,0,0,0,0,0,0],
}

def print_Matrix():
  line ="     "
  for i in range(0, len(game.STATES)):
    line += str(game.STATES[i][1]) + str(game.STATES[i][2]) + str(game.STATES[i][3]) +"   "
  line += "11x   xxx  else"
  print(line)
  print("    ----------------------------------------------------------")
  for i in range(0, len(MATRIX.keys())):
    line = str(i) + " | "
    for j in range(0, len(MATRIX[i])):
      if (int(MATRIX[i][j]) < 1000):
        line += " "
      if (int(MATRIX[i][j]) < 100):
        line += " "
      if (int(MATRIX[i][j]) < 10):
        line += " "

      line += str(int(MATRIX[i][j]))+", "
    print(line)



# find index in STATES of the given state
def state_index(state):
  for i, item in enumerate(game.STATES):
    if(game.STATES[i][0] == state[0] and game.STATES[i][1] == state[1] and game.STATES[i][2] == state[2]):
      return i
  if (state[0] == 1 and state[1] == 1):
    return 7
  elif (state[0] == state[1] and state[1] == state[0]):
    return 8
  else: 
    return 9

# find index in ACTIONS of the given action
def action_index(action):
  for i, item in enumerate(game.ACTIONS):
    if(game.ACTIONS[i][0] == action[0] and game.ACTIONS[i][1] == action[1] and game.ACTIONS[i][2] == action[2]):
      return i

# find the index of the best action in the MATRIX for given state
def best_action_index(state):
  state_idx = state_index(state)
  state_actions_values = [MATRIX[0][state_idx]]
  for i in range(0, len(MATRIX)):
    state_actions_values = [MATRIX[i][state_idx]]
  return  state_actions_values.index(max(state_actions_values))


# changes the value of q_table for state/action couple
def update_Matrix(state, action, next_state):
  best_next_action= best_action_index(next_state)
  state_index = state_index(state)
  action_index = action_index(action)
  Qvalue = (1-learning_rate) * MATRIX[action_index][state_index] + learning_rate * (game.reward(state, True) + gamma * MATRIX[best_next_action][state_index(next_state)])
  MATRIX[action_index][state_index] = Qvalue

def epsilon(e):
  # exploitation
  if random.uniform(0, 1) > e:
    return False
  # exploration
  else:
    return True

def learn_episode():
  # an episode is composed of 3 rounds
  # first round where we roll every dices
  current_state = sorted([random.randint(1,6), random.randint(1,6), random.randint(1,6)])
  # two more rounds
  for i in range(0, 2):
    if (epsilon(epsilon)):
      current_state = sorted(explore(current_state))
    else: 
      current_state = sorted(exploit(current_state))
  return current_state

# play a random action and updates the MATRIX 
def explore(state):
  action = game.ACTIONS[random.randint(0,7)]
  next_state = game.transition(state, action)
  update_Matrix(state, action, next_state)
  return next_state

# choose the best action to play
def exploit(state):
  state_id = state_index(state)
  state_actions_values = [None] * len(MATRIX)
  for i in range(0, len(MATRIX)):
    state_actions_values[i] = [MATRIX[i][state_id]]
  # find the index of the best action
  best_action_index = state_actions_values.index(max(state_actions_values))
  action_to_play = game.ACTIONS[best_action_index]
  next_state = game.transition(state,action_to_play)
  return next_state

def play_n_episodes(n):
  for i in range(0, n):
    learn_episode()


play_n_episodes(100000)
print_Matrix()