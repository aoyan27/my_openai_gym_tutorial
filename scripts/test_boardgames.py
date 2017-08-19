#!/usr/bin/env python
#coding:utf-8

import gym

env = gym.make('Go9x9-v0')
env.reset()
env.render()
