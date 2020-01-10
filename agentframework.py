
"""
This file Create by Fawziah Almutairi 
Created on Mon Dec 16 01:25:40 2019.
Programming for Geographical Information Analysts: Core Skills.
@author: ml18fksa, the Student ID is 201288865.
Geography Programming Courses at University of Leeds.
 
"""
"""
agentframework.py defines a class Agents. 
1. The initialisation of the class takes arguments environment, agents 
2. The calss has methods move, eat at 2D environment.

This file called the  agentframework which has agents at the environment.
The main task for this model is class agent to moving and eating to sharing resources and exchange resources with agents neighbourhood.
"""
"""
 import the agent with function random. 
________________________________________________
"""
import random

"""
 class the agents at the environment in the in.txt file.
_________________________________________________________ 
"""
class Agents():
   
    def __init__(self,i,agents,environment):
        self.i = i
        self.x = random.randint(0,250)
        self.y = random.randint(0,250)
        self.environment = environment
        self.agents =agents
        self.store = 0
       
        
#################################
#deinition to move the agents #
#The Agents have y and x coordinates.#
######################################

    def __str__(self):   
        return "Agent(i=" + str(self.i)+ ", store=" + str(self.store) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")"  

    def move(self): #Move function
        
        r = random.random()
        
        if r < 0.5:
            
            self.y += 1
        else:
            self.y -= 1

        r = random.random()
        
        if r < 0.5:
          
             self.x += 1
        else:
          
              self.x -= 1
    
##################################################
##deinition to eat the agents at 2D environment.#
#################################################
    def eat(self): #eat function
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
#######################################################
#deinition to get distance the agents with coordinates.#
#######################################################
    def get_distance(self, agent): #distance function
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
#############################################################
# deinition to share the agents distance with neighbourhood#
##############################################################
    def share(self, d):
        for agent in self.agents:
            if agent != self:
                dis = self.get_distance(agent)
                if (dis < d):
                    print(self, "is sharing with", agent,  "as distance is", dis)
                    total = self.store + agent.store
                    ave = total/2
                    self.store = ave 
                    agent.store = ave
