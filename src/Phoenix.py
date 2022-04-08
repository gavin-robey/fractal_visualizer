from Fractal import Fractal


class Phoenix(Fractal):

    def __init__(self, iterations):
        self.iterations = iterations

    def count(self, c):
        count = 0
        z = complex(0, 0)
        for i in range(self.iterations):
            z = z * z + c # change this to work with the formula
            if abs(z) > 2:
                count += i
                return count
        return count - 1
