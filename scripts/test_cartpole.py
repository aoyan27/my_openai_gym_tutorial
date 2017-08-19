#!/usr/bin/env python
#coding:utf-8

import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
    print "observation : ", observation, " reward : ", reward, " done : ", done, " info : ", info
    """
    observation : 行動した後の状態(next_state)
    reward : 報酬
    done : 'env'において定義されたしきい値に応じて、そのエピソードを打ち切るためのフラグ
    info : 学習を行う際の詳細情報を記載できる(自分の自由に？公式に提供されている環境では何も入っていない)
    """

    #  print "env.observation_space : ", env.observation_space
    #  print "env.action_space. : ", env.observation_space
