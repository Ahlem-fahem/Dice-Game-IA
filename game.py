import random
STATES = [
  {
    "Reward": 800,
    "1": 4,
    "2": 2,
    "3": 1}, 
  {
    "Reward": 700,
    "1": 1,
    "2": 1,
    "3": 1}, 
  {
    "Reward": 203,
    "1": 1,
    "2": 2,
    "3": 3}, 
  {
    "Reward": 204,
    "1": 2,
    "2": 3,
    "3": 4}, 
  {
    "Reward": 205,
    "1": 3,
    "2": 4,
    "3": 5
  }, 
  {
    "Reward": 206,
    "1": 4,
    "2": 5,
    "3": 6
  }, 
  {
    "Reward": 0,
    "1": 2,
    "2": 2,
    "3": 1
  }]

# True = Roll the dice  , False= keep the dice
ACTIONS = [
  [False, False, False],
  [False, False, True],
  [False, True, False],
  [False, True, True],
  [True, False, False],
  [True, False, True],
  [True, True, False],
  [True, True, True]
]

def reward(state, roll):
  # the reward is given just after rolling dices 
  if (roll == False):
    return 0
  else:
    for i in enumerate(STATES):
      # if the state is one of the constent STATES , return the reward 
      if(STATES[i][1] == state[1] and STATES[i][2] == state[2] and STATES[i][3] == state[3]): 
        # return the Reward
        return STATES[i][0]
    #  the 11x case
    if (state[0] == 1 and state[1] == 1):
      # reward is 400 + x
      return 400+state[2]
    # the xxx case
    elif (state[0] == state[1] and state[1] == state[0]):
      # reward is 300 + x
      return 300 + state[0]
    else: 
      # reward is 100 + highest value of dice
      return 100+state[2]
    

def transition(state, action):
  next_state = [None] * 3
  for i, item in enumerate(action):
    # the agent chose to roll the dice
    if (item == True):
      next_state[i] = random.randint(1,6)
    else:
      next_state[i] = state[i]

  return sorted(next_state)