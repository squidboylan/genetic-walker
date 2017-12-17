#!/usr/bin/env python
import gym
env = gym.make('BipedalWalker-v2')
print(env.action_space)
print(env.observation_space)
print(env.action_space.low)
print(env.action_space.high)
print(env.observation_space.low)
print(env.observation_space.high)
"""
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        #print(observation)
        action = env.action_space.sample()
        print(action)
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
"""
