# Learn the basics about how to define an environment or get an observation from the environment
import random

class Environment:
    """ This environment will give random rewards to the agent  regardless of its actions """

    def __init__(self):
        self.steps_left = 10

    def get_observations(self):
        return [0.0,0.0,0.0]

    def get_actions(self):
        return [0,1]
    
    def is_done(self):
        return self.steps_left == 0

    def action(self):
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()

class Agent:

    def __init__(self):
        self.total_reward = 0.0

    def step(self,env):
        current_obs = env.get_observations()
        actions = env.get_actions()
        reward = env.action()
        self.total_reward += reward
        

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print(f"Total reward got: {agent.total_reward:.2f}")
