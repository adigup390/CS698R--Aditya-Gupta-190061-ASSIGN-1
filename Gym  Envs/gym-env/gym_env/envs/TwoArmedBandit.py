import gym
from gym import spaces
from gym.utils import seeding

class twoarmedbandit(gym.Env):
  # metadata = {'render.modes': ['human']}

  def __init__(self,alpha,beta,seed_):
    super(twoarmedbandit,self).__init__()

    self.action_space = spaces.Discrete(2)
    self.observation_space = spaces.Discrete(1)
    self.alpha = alpha
    self.beta = beta
    self.seed(seed_)
  
  def seed(self,seed_):
    self.np_random, seed_ = seeding.np_random(seed_)

  def step(self,action):

    # 0 ->left action
    # 1 ->right action

    if action==0 :
      reward = self.np_random.binomial(1,self.alpha,None)

    else:
      reward = self.np_random.binomial(1,self.beta,None)

    return 0, reward, True, {}

  def reset():
     return 0
