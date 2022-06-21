import gym
from gym import spaces
from importlib_metadata import metadata
import numpy as np
from ipdb import set_trace

class boxsystem(gym.Env):
    metadata = {'render.modes':['human']}


    def __init__(self, sys, fixed_start=False, normalized_actions=False):
        self.sys = sys
        self.fixed_start

    def step(self,  actions):
        print('')

    def reset(self):
        metadata.reset()
