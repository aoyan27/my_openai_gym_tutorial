#!/usr/bin/env python
#coding:utf-8

import gym

env = gym.make('Humanoid-v1')
env.reset()
env.render()
