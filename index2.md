---
title: Test
---


The program is written in the Python language using Spyder (Python 3.6). 
The program creates a model, a simple Agent Based Model (ABM) built on 
a place. Essentially, the model is made up of ten randomly located agents 
(picture it as a flock of sheep) which move, and feed a hundred times 
off the environment. The agents are aware of each other and do not 
interfere in the munching of the environment by other agents. Each 
munch is the equivalent of ten units of the environment, thus for 
every move an agent makes, the environment is reduced by ten units.

The model has two variables; agents, and environment. The agents are 
generated using random coordinates. The environment is a 300 by 300 
raster grid created from 'in.txt', a csv file of 300 rows and 300 
columns of numeric data made available by Dr Andy Evans on the practicals 
section of the University of Leeds' Geography Programming Courses website. 

A loose coupling, and high cohesion method was adopted for the program. 
The loose coupling approach integrates the functionality of one tool into 
another (Wittman, 2000). The loose coupled architecture supports easy 
exchange of class components. It facilitates a wide range of spatial 
processing services which can be modified later without requiring 
fundamental changes to the architecture (Krämer & Senner, 2015). High 
cohesion of the classes indicates that all elements of a class are 
related to each other, that they are grouped logically, and that they 
achieve a common goal (von Hohenrain LU, 2006). Two classes are used 
in this program; the model (model.py), and the Agent class 
(agentframework.py), see Fig. 1. The model class which is a 
superclass, is made up of only two variables; the agents, and the 
environment. The coordinates of the agents are generated in the Agent 
class. The methods of the program; move, eat, distance_between, and 
share_with_neighbours are encapsulated in the Agent class. The program 
has a high cohesion given that the coordinates of the agents, and all the 
methods are in the Agent class.

Fig. 1:
![alt text](https://odohemma.github.io/ClassDiagramforABM.png "UML of the Agent Based Model")







[here](https://odohemma.github.io/model.py)