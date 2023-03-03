from drunk import Drunk

class Bird(Drunk):
    returns = [0]
    distances = [0]
    position = (0,0,0)
    moves = [(-1,0,0), (0,-1,0), (0,0,-1), (1,0,0), (0,1,0), (0,0,1)]
