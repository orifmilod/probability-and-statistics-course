import time

from simulation import Canvas 
from visualization import Visualization 

from game_of_life import GameOfLife 

canvas = Canvas()
visualization = Visualization()
automata = GameOfLife()

for i in range(0, 50):
    canvas.step(automata)
    visualization.draw(canvas.pixels)
