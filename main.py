from setup import *

num_of_cases= 15
num_of_rocks= 50
troll_pos= num_of_cases// 2
env= Env(num_of_cases, num_of_rocks, troll_pos)
env.simulateGame('random100', 'random100')