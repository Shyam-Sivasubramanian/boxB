import gym
from gym import Env
import numpy as np
from gym import spaces
import random

class BoxSystem(Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes' : ['human']}

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


    def __init__(self, x=5, y=5):
        self.size = np.array([x,y]) #size of the grid
        self.window = 512 #size of the pygame window
        self.action_space = spaces.Discrete(4) # 4 actions (right, up down and left)
        self.target_pos = np.array([x,y]) #position of the target (x and y coords)
        self.observation_space = spaces.Box(low=0, high=self.size, shape =(2,), dtype=np.float32)


    def reset(self, poserx = random.randint(0,5), posery = random.randint(0,5)): #resets so that the agent positions itself to a random point on the grid 
        self.agent_pos = np.array([poserx, posery]) # defines the x and y acoords of the pos  
        return self.agent_pos #returns as a numpy array


    def step(self, action):
        #deals with each of the 4 actions that the agent can take
        

        if(action == self.UP):
            self.agent_pos[1] +=1
        elif (action == self.DOWN):
            self.agent_pos[1] -=1
        elif(action == self.LEFT):
            self.agent_pos[0] -=1
        elif(action == self.RIGHT):
            self.agent_pos[0] +=1
        else: 
            raise ValueError("Received invalid action={} which is not part of the action space".format(action))
        
        #deals with the boundaries of the grid
        self.agent_pos = np.clip(self.agent_pos, 0, self.size[1])

        done = bool(self.agent_pos[0] == self.target_pos[0] and self.agent_pos[1] == self.target_pos[1]) # if the agent pos is the same as the target pos

        reward = -(((self.target_pos[0] - self.agent_pos[0]) + (self.target_pos[1] - self.agent_pos[1])) ** 0.5) #uses the distance formula
        """if the dist between the agent and the target = 0 then it will be the largest reward, otherwise everything will be a negative number """

        info={} # i'm not using this


        return np.array([self.agent_pos[0], self.agent_pos[1]]), reward, done, info #return everything




            

    def render(self, mode = 'human'):
        pass
        



    def close(self):
        pass
