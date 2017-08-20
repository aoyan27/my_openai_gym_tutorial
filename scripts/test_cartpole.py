#!/usr/bin/env python
#coding:utf-8

#################################################
#
#   Tutorial-1('Running an environment' section)
#
#################################################
#  import gym
#  env = gym.make('CartPole-v0')

#  env.reset()
#  for _ in range(1000):
    #  env.render()
    #  observation, reward, done, info = env.step(env.action_space.sample())
    #  print "observation : ", observation, " reward : ", reward, " done : ", done, " info : ", info
    #  """
    #  observation : 行動した後の状態(next_state)
    #  reward : 報酬
    #  done : 'env'において定義されたしきい値に応じて、そのエピソードを打ち切るためのフラグ
    #  info : 学習を行う際の詳細情報を記載できる(自分の自由に？公式に提供されている環境では何も入っていない)
    #  """

    #  #  print "env.observation_space : ", env.observation_space
    #  #  print "env.action_space. : ", env.observation_space


#################################################
#
#   Tutorial-2('Observations' section)
#
#################################################
#  import gym
#  env = gym.make('CartPole-v0')
#  for i_epidode in range(20):
    #  observation = env.reset()
    #  for t in range(100):
        #  env.render()
        #  print (observation)
        #  action = env.action_space.sample()
        #  observation, reward, done, info = env.step(action)
        #  if done:
            #  print ("Episode finished after {} timesteps.".format(t+1))
            #  break


#################################################
#
#   Tutorial-3('Spaces' section)
#
#################################################
#  import gym
#  env = gym.make('CartPole-v0')
#  print (env.action_space)

#  print (env.observation_space)

#  print (env.observation_space.high)
#  print (env.observation_space.low)
#  """
#  spaceというパッケージがある、このパッケージにあるモジュールを使って、OpenAI Gymは状態や行動の定義を表している。
#  Discrete : 0からn-1までの負の数を含まない範囲の値を表す。
    #  使い方は、
        #  >> from gym import spaces
        #  >> a = spaces.Discrete(10)  #0~9の範囲の値を考慮する
        #  >> a.sample() #0~10の中からランダムに値を選択する
        #  >> a.contains(5) #引数が設定した範囲内にあるかTrue or Falseで返してくる
#  Boxes : n次元のboxをあつかう。
    #  例えば、
        #  1. Box(-1.0, 1.0, (3,4)) # low and high are scalars, and shape is provided
        #  2. Box(np.array([-1.0,-2.0]), np.array([2.0,4.0])) # low and high are arrays of the same shape
        #  のような使い方においては、
        #  1. 3x4次元の配列が確保され、それぞれの要素の最小値、最大値が第一引数、第二引数となっている
        #  2. 2x2次元の配列が確保され、それぞれの要素の最大値、最小値は引数である配列の値となっている
        
    #  --->envでは、'observation_space'や'action_space'として利用されており、
        #  状態や行動の型(何次元配列で定義されているか)や、その値の上限、下限値を知ることができる
#  """


#################################################
#
#   Tutorial-4('Environments' section)
#
#################################################
#  import gym
#  print (gym.envs.registry.all())
#  """
#  gym.envs.registry.all()で登録されている環境のリストを確認できる。
#  大元のgym/gym/envs/の中にある__init__.pyの中でgym.envsがimportされた時の初期化処理として、
#  'registration.py'におけるregistor関数を利用して、環境のidや報酬のしきい値、最大episode数、などを登録している。
#  そうすると、'env = gym.make('自分で登録した環境の名前')'で環境を利用できるようになる。

#  """


#################################################
#
#   Tutorial-5(Recoding results'' section)
#
#################################################
import gym
from gym import wrappers
env = gym.make('CartPole-v0')
env = wrappers.Monitor(env, '/tmp/cartpole-experiment-1') #上の行の環境を定義している変数envをwrappr.Monitorクラスで上書きしているイメージ
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps.".format(t+1))
            break
