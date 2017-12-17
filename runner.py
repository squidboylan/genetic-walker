#!/usr/bin/env python3

import yaml
import os
import sys
import gym

def test_genomes(file_name):
    env = gym.make('BipedalWalker-v2')
    observation = env.reset()
    final_reward = 0

    with open(file_name, 'r') as file_stream:
        actions = yaml.load(file_stream)

    for t in range(2000):
        action = actions[t % len(actions)]
        observation, reward, done, info = env.step(action)
        print(reward)
        final_reward = final_reward + int(reward)

    final_yaml = {"reward": final_reward}

    with open(file_name + '-result', 'w') as file_stream:
        actions = yaml.dump(final_yaml, file_stream)

if __name__ == "__main__":
    file_name = sys.argv[1]
    test_genomes(file_name)
