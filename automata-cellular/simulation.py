import random

class Canvas:
    def __init__(self, height = 500, width = 500, density = 0.5, seed = 0):

        self.height = height
        self.width = width

        if seed != 0:
            random.seed(seed)
        else:
            random.seed()
        
        self.pixels = [[(1 if random.randint(1, int(1/density)) == 1 else 0) for i in range(0, self.height)] for j in range(0, self.width)]

    def step(self, automata):
        def calculate_pixel(i, j):
            internal_sum = 0
            for offset_y in range(-1,2):
                for offset_x in range(-1,2):
                    if i + offset_y >= 0 and i + offset_y<self.height:
                        if j + offset_x >= 0 and j + offset_x<self.width:
                            internal_sum += self.pixels[i + offset_y][j + offset_x]*automata.matrix[1 + offset_y][1+offset_x]
            return automata.activation(internal_sum)
        updated_pixels = [[(calculate_pixel(i,j)) for i in range(0, self.height)] for j in range(0, self.width)]

        self.pixels = updated_pixels
