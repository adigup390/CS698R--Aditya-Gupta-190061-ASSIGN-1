import gym
from gym import spaces
from gym.utils import seeding

class RWE(gym.Env):
  def __init__(self,initial_state,seed_):
    super(RWE,self).__init__()

    self.action_space = spaces.Discrete(2)
    self.observation_space = spaces.Discrete(5)
    self.seed(seed_)
    self.state = initial_state
    if self.state!=0 and self.state!=6:   self.done = False
    else: self.done = True 

  def seed(self,seed_):
    self.np_random, seed1 = seeding.np_random(seed_)
    return [seed1]

  def step(self,a):

    if self.done: return self.state,0,True,{}

    action = self.np_random.choice(2,size = None,p = [0.5,0.5])

    #0 - left action
    #1 - right action

    if action==0: self.state = self.state - 1
    else: self.state = self.state + 1

    if self.state!=0 and self.state!=6:   self.done = False
    else: self.done = True 

    reward = 0
    if self.state==6: reward = reward + 1

    return self.state, reward, self.done,{}

  def reset(self):
    self.state = 1
    self.done = False
    return self.state,self.done