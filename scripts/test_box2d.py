#!/usr/bin/env python
#coding:utf-8

import gym

env = gym.make('LunarLander-v2')
env.reset()
env.render()
