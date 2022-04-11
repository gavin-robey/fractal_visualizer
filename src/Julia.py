from Fractal import Fractal


class Julia(Fractal):
    '''
    This class applies the algorithms of Julia.
    '''

    def __init__(self, iterations, creal, cimag):
        self.iterations = iterations
        self.creal = creal
        self.cimag = cimag

    def count(self, z):
        '''
        This method loops through the length of the iterations given and depending on some magic from the julia algorithm
        it returns the number of iterations
        '''
        count = 0
        c = complex(self.creal, self.cimag)
        for i in range(self.iterations):
            z = z * z + c
            if abs(z) > 2:
                count += i
                return count
        return count - 1
