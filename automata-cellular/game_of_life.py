class GameOfLife:
    matrix = [[1,1,1], [1,9,1], [1,1,1]]

    def activation(self, internal_sum):
        return 1 if (internal_sum == 3 or internal_sum == 11 or internal_sum == 12) else 0
