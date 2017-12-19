#!/usr/bin/env python3

import ujson
import os
import sys
import gym

def test_creature(file_name):
    env = gym.make('BipedalWalker-v2')
    observation = env.reset()
    final_reward = 0

    with open(file_name, 'r') as file_stream:
        actions = ujson.load(file_stream)

    for t in range(2000):
        action = actions[t % len(actions)]
        observation, reward, done, info = env.step(action)

        final_reward = final_reward + float(reward)

    final_ujson = {"reward": final_reward}

    with open(file_name + '-result', 'w') as file_stream:
        actions = ujson.dump(final_ujson, file_stream)

if __name__ == "__main__":
    file_name = sys.argv[1]
    test_creature(file_name)
