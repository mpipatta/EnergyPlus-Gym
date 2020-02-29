
import gym
import eplus_env
import pandas as pd 
# env = gym.make('Eplus-demo-v1')
# curSimTime, ob, isTerminal = env.reset() # Reset the env (creat the EnergyPlus subprocess)
# while not isTerminal:
#     action = [20, 20]
#     curSimTime, ob, isTerminal = env.step(action)
#     print(curSimTime, ob)

# env.close()

alist = []
env = gym.make('Eplus-demo-v2')
curSimTime, ob, isTerminal = env.reset() # Reset the env (creat the EnergyPlus subprocess)
while not isTerminal:
    action = [20]
    curSimTime, ob, isTerminal = env.step(action)
    alist.append(ob)
    print(curSimTime, ob)

df=pd.DataFrame(alist, index=None, columns=['Tout','T1','T2','T3','T4','P1','P2','P3','P4'])
df.to_csv('output.csv')
env.close()