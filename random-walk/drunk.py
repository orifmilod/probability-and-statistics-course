import random

class Drunk:
    def move(self):
        move = self.moves[random.randint(0, len(self.moves) - 1)]
        self.position = self._add_tuples(self.position, move)
        self.register_move()

    def _add_tuples(self, a, b):
        return tuple(map(lambda i, j: i + j, a, b))

    def is_at_origin(self):
        for i in range(0, len(self.position)):
            if not self.position[i] == 0:
                return False

        print("At origin: " + str(self.position) + " in step " + str(len(self.returns)))
        return True

    def calculate_distance(self):
        distance_sq = 0
        for i in range(0, len(self.position)):
            distance_sq += self.position[i]**2

        return distance_sq**0.5

    def register_move(self):
        self.returns.append(self.returns[-1])
        if self.is_at_origin():
            self.returns[-1]+=1

        self.distances.append(self.calculate_distance())
