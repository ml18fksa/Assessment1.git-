"""
This file Create by Fawziah Almutairi 
Created on Mon Dec 16 01:25:40 2019
Programming for Geographical Information Analysts: Core Skills.
@author: ml18fksa, the Student ID is 201288865
Geography Programming Courses at University of Leeds 
""
This file called the GUI which means  build  a Graphical User Interface at 2D environment.
The main task for this model is displays in a window with a list of agents which has number of  animals eat and move at 2D environment
sharing resources and exchange resources with agents neighbourhood based on a green landscape of the environment. 
"""
"""
using import to get code from anther python packages and moudules.
the imports sould be in the top of the moudle.
"""

"""
Step(1) import the libraries and files it is the main step.
"""
import agentframework
import random
import operator
import matplotlib.pyplot
import tkinter
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.animation
import csv
import requests
import bs4

"""
Step(2)to request the data from the web Page.
"""

def request_data():
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)
    
"""
Step(3) Make the agents in GUIs.
"""   
# setting frameworks#
num_of_agents = 10 #the number of agents in a graph#
num_of_iterations = 100 # the number of iterations in the environment graph#
dist=20 # neighbourhood with 20 distance to sharing the environment#
agents = []
# to create agents in empty list#
#import environment data#
environment = []

#to make agents to produce similar outcome when it is run.
random.seed(1)

"""
Step(4)to Read the file 
"""
#to open in.txt file
f = open("in.txt") 
# data define to csv file to read the environment 
data = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in data:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
    
f.close() #to close the  in.txt file after run it#
 
"""
Step(5) A command to calculate the distance.
deinition to distance the agents that have y and x coordinates.
"""      
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

"""
Step(6)Communication with the 2D environment.
"""
# the way to creating agents list in the graph.
for i in range(num_of_agents):
    agents.append(agentframework.Agents(i, agents, environment))
# to carry on in agents movement.
carry_on = True

"""
Step(7)To class the number of agents to moving and eating to sharing with enviroment in 2D inplotting. 
TO Display the white Agents 
"""
def update(frame_number):
    global carry_on
    
#Clear the figure
    fig.clear()
    
# Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
    
            agents[i].move()
            agents[i].eat()
            agents[i].share(dist)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="white")
    matplotlib.pyplot.imshow(environment)#share_with_neighbours(neighbourhood)
#matplotlib.pyplot.show()
 
"""
Step (8) deinition to get function of the agents in the librarie.
To display the animation 
"""

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a	# Returns control and waits next call.
        a = a + 1             
#create figure import automatically 
        
fig = matplotlib.pyplot.figure(figsize=(7, 7))

#To display the animation 

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()
# Just showing menu elements 

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
  
"""
Step (9) create root window.

To display a Graphical User Interface(GUI) model.

"""  
# to create root window in the model
root = tkinter.Tk()  
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
tkinter.mainloop() 
# Wait for interactions

        