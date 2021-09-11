from gym.envs.registration import register

register(
    id='two-v0',  # This will the id with which we will refer to your enviroment.
    # This is the name of the actual class defined in bandit_walk.py where we implement the code for our environment.
    entry_point='gym_env.envs:twoarmedbandit',
)
register(
    id='ten-v0',  # This will the id with which we will refer to your enviroment.
    # This is the name of the actual class defined in bandit_walk.py where we implement the code for our environment.
    entry_point='gym_env.envs:tenarmedbandit',
)
register(
    id='RWE-v0',  # This will the id with which we will refer to your enviroment.
    # This is the name of the actual class defined in bandit_walk.py where we implement the code for our environment.
    entry_point='gym_env.envs:RWE',
)
