#!/usr/bin/env python
#coding:utf-8

import numpy as np

import gym

env = gym.make('Reacher-v1')

print "env.observation_space : ", env.observation_space
print "env.action_space : ", env.action_space

for i in xrange(1000):
    observation = env.reset()
    for  j in xrange(1000):
        env.render()

        state = observation
        action = env.action_space.sample()
        #  action = np.array([2.0])
        print type(action)
        observation, reward, done, info = env.step(action)
        next_state = observation
        print "state : {0}, action : {1}, next_state : {2}, reward : {3}, done : {4}, info : {5}".format(state, action, next_state, reward, done, info)

        #  if done:
            #  break


