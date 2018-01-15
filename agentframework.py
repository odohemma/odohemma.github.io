# -*- coding: utf-8 -*-
"""
The following classes and functions are defined in this module;

Agent:
This class secures environment, agents and store variables.

move:
This function moves an agent by one step in a random direction.

eat:
Subject to availability, agents nibble ten units of the environment.

distance_between:
This function calculates the distance between any two agents.

share_with_neighbours:
This allows two agents to evenly share stored units of environment.
"""
import random
import csv


environment = []
with open('in.txt', newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)


agents = []


class Agent():
    def __init__ (self, environment, agents):
        """
        This class secures environment, agents and store variables.
        The coordinates of the agents are defined here.
        
        Instance variables:
        environment -- it represents the environment dataset
        agents -- it represents the agents list
        """
        
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)

       
    def move(self):
        """
        This moves an agent by one step in a random direction.
        
        An agent that leaves from the top of the environment, comes in 
        at the bottom, and vice versa.
        An agent that leaves from the right side of the environment, 
        comes in from the left, and vice versa.
        """
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    
    def eat(self): 
        """
        This enables an agent to nibble 10 units of the environment, 
        and increasing it's store by the same amount after making a 
        step.  However, this only occurs if there are 
        over ten units of environment at the agent's location.
        """
        
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10


    def distance_between(self, agent):
        """
        This calculates distance.
        
        Returns:
        The distance between two agents.
        """
        
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
 
    
    def share_with_neighbours(self, neighbourhood):
        """"
        This enables any two agents that are 20 steps away to evenly 
        share units of the environment they have both stored within 
        themselves.
        
        Prints:
        sharing 'distance' 'average units of environment'
        """
        
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                sum = self.store + agent.store
                average = sum/2
                self.store = average
                agent.store = average
                print("sharing " + str(distance) + " " + str(average))
            