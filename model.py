# -*- coding: utf-8 -*-
"""
This creates 10 agents that move and eat 100 times in random direction.
It also produces an animation of the agents in motion.

Instructions:
Run agentframework.py before you run this file.
"""

import random
import operator
import csv
import matplotlib.pyplot
import matplotlib.animation
import agentframework


# This imports a csv file and reads it into an environmnet list in 2D.
environment = []
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        
        
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


# This makes and populates the agents' list.
# The agents are represented as objects in the list.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
  

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
# The agents eats and stores 10 units of the environment.
        agents[i].eat()                        
        agents[i].share_with_neighbours(neighbourhood)


# Plots the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


# An animation of the moving agents is created here
num_of_agents = 10
num_of_iterations = 100
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

def update(frame_number):
    
    fig.clear()   

    for i in range(num_of_agents):
            if random.random() < 0.5:
                agents[i][0]  = (agents[i][0] + 1) % 99 
            else:
                agents[i][0]  = (agents[i][0] - 1) % 99
            
            if random.random() < 0.5:
                agents[i][1]  = (agents[i][1] + 1) % 99 
            else:
                agents[i][1]  = (agents[i][1] - 1) % 99 
        
   
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
        print(agents[i][0],agents[i][1])


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, 
   repeat=False, frames=num_of_iterations)

matplotlib.pyplot.show()








