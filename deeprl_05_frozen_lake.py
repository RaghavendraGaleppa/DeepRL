import gym
import collections

ENV_NAME = "FrozenLake-v0"
GAMMA = 0.9
TEST_EPISODES = 20

class Agent:
    def __init__(self):
        self.env = gym.make(ENV_NAME)
        self.state = self.env.reset()
        self.rewards = collections.defaultdict(float)
        self.transits = collections.defaultdict(collections.Counter)
        self.values = collections.defaultdict(float)

    def play_n_random_steps(self, count):
        for _ in range(count):
            action = self.env.action_space.sample()
            new_state, new_reward, is_done, _ = self.env.step(action)
            self.rewards[(self.state,action,new_state)] = new_reward
            self.transits[(self.state,self.action)][new_state] = +1
            self.state = self.env.reset() if is_done else new_state
