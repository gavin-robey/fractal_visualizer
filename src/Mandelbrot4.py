from Fractal import Fractal


class Mandelbrot4(Fractal):
    '''
    This class applies the algorithms of Mandelbrot4.
    '''

    def __init__(self, iterations):
        self.iterations = iterations

    def count(self, c):
        '''
        This method loops through the length of the iterations given and depending on some magic from the julia algorithm
        it returns the number of iterations
        '''
        count = 0
        z = complex(0, 0)
        for i in range(self.iterations):
            z = (z * z * z * z) + c
            if abs(z) > 2:
                count += i
                return count
        return count - 1