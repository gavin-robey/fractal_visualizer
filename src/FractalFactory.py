from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot3 import Mandelbrot3
from Mandelbrot4 import Mandelbrot4


class FractalFactory:
    '''
    This class creates a default fractal configuration dictionary, if nothing is passed in.
    Otherwise, the configuration is set to the input value.
    Then it uses this dictionary to build a Fractal concrete class and returns this class.
    '''

    def __init__(self):
        self.__defaultFractal = {
            "type": "mandelbrot",
            "pixels": 512,
            "centerx": -1.40812110900879,
            "centery": -0.136344909667969,
            "axislength": 0.0028839111328125,
            "iterations": 256,
            "name": "default"
        }
        self.configuration = self.__defaultFractal

    def makeFractal(self, configurationDict=None):
        '''
        This method finds out if a configuration Dictionary is given, if it is not then it uses the default fractal configuration
        dictionary. If a configuration dictionary is given then this is the configuration dictionary that will be used.
        Depending on the type given from this configuration dictionary, a selected Fractal class will be returned.
        '''
        if configurationDict is not None:
            self.configuration = configurationDict

        if self.configuration["type"] == "mandelbrot":
            return Mandelbrot(self.configuration["iterations"])
        elif self.configuration["type"] == "julia":
            return Julia(self.configuration["iterations"], self.configuration['creal'], self.configuration['cimag'])
        elif self.configuration["type"] == "mandelbrot3":
            return Mandelbrot3(self.configuration["iterations"])
        elif self.configuration["type"] == "mandelbrot4":
            return Mandelbrot4(self.configuration["iterations"])


