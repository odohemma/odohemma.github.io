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

Fig. 1: UML of the Agent Based Model
![alt text](https://odohemma.github.io/ClassDiagramforABM.png "UML of the Agent Based Model")

The splitting of the program into different classes provides an efficient 
and functional program. It also separates and isolate critical variables, 
methods, and functions into a subclass, thus protecting the critical 
components of the program from users, without negating the purpose and 
aims of the program was designed to achieve. Given that the program was 
coded in Spyder, all syntaxerrors were spotted, and eliminated. Similarly, 
all issues with runtime logic were spotted, and eliminated.

The code was written to be a double-click-to-run program, the user does 
not need to input data for the program to run. The usbility of the 
program was designed to be as effective, and efficient as possible. 
Though it is a double-click-to-run program, users can vary the number 
of agents, and the number of times the agents move and eat by varying 
the num_of_agents, and the num_of_iterations variables respectively. A 
determinant for the usability of a program is the number of clicks 
required to run it (Istvan, 2012); based on this criteria, the program 
has a good usability as it requires two clicks to run.



**References**
---
Istvan, S., 2012. Comparison Of The Most Popular Open-Source GIS Software In The Field Of Landscape Ecology. *AGD Landscape & Environment*, 6(1), pp. 76-94.

Krämer, M. & Senner, I., 2015. A Modular Software Architecture for Processing of big Geospatial Data in the Cloud. *Computers & Graphics*, Volume 49, pp. 69-81.

von Hohenrain LU, D. I., 2006. *IPODLAS A Framework for Coupling Temporal Simulation Systems, Virtual Reality, and Geographic Information System*. Ph.D. thesis: University of Zurich.

Wittman, J., 2000. Simulation Model and Geographic Information System : Coupling Alternatives at the Practical Example. In: A. Cremers & K. Greve, eds. *Umweltinformatik*. Metropolis-Verlag, Bonn: Internationales Symposium, pp. 45-48.








[here](https://odohemma.github.io/model.py)