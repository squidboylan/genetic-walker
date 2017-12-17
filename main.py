#!/usr/bin/env python3

import gym
import sys
import yaml

env = gym.make('BipedalWalker-v2')
file_name = sys.argv[1]
observation = env.reset()

with open(file_name, 'r') as file_stream:
    actions = yaml.load(file_stream)

for t in range(2000):
    env.render()
    action = actions[t % len(actions)]
    observation, reward, done, info = env.step(action)
    print(reward)
