import gym
from gym import spaces
from gym.utils import seeding

class tenarmedbandit(gym.Env):

  def __init__(self,sigma,seed_):
    super(tenarmedbandit,self).__init__()

    self.action_space = spaces.Discrete(10)
    self.observation_space = spaces.Discrete(1)
    self.seed(seed_)
    self.Q_star = self.np_random.normal(0,sigma,10)

  def seed(self,seed_):
    self.np_random, seed1 = seeding.np_random(seed_)
    return [seed1]

  def step(self,a):

    reward = self.np_random.normal(self.Q_star[a],1,size = None)

    return 0,reward,True,{}
  def reset():
    pass