from Palette import Palette
from colour import Color
import math


class Rainbow(Palette):
    '''
    This class creates a color palette, then returns a single color from this color palette
    It does this by using the colour module, and appending a range of colors from one value to another.
    For more variation multiple colors are given and multiple ranges are set.
    Each range is added to the palette array.
    Each range is in a loop that runs to the length of 'iterations' divided by how many ranges there are.
    '''

    def __init__(self, iterations):
        self.__iterations = iterations
        self.__palette = []
        gray = Color('gray')
        white = Color('white')
        navy = Color('#292961')
        yellow = Color("yellow")
        cyan = Color('cyan')
        magenta = Color('magenta')
        black = Color('black')
        steps = math.ceil(self.__iterations / 11)
        self.__palette = [c.hex_l for c in white.range_to(navy, steps)]
        self.__palette += [c.hex_l for c in navy.range_to(cyan, steps)]
        self.__palette += [c.hex_l for c in gray.range_to(black, steps)]
        self.__palette += [c.hex_l for c in black.range_to(yellow, steps)]
        self.__palette += [c.hex_l for c in yellow.range_to(black, steps)]
        self.__palette += [c.hex_l for c in black.range_to(cyan, steps)]
        self.__palette += [c.hex_l for c in cyan.range_to(black, steps)]
        self.__palette += [c.hex_l for c in black.range_to(navy, steps)]
        self.__palette += [c.hex_l for c in navy.range_to(black, steps)]
        self.__palette += [c.hex_l for c in black.range_to(magenta, steps)]
        self.__palette += [c.hex_l for c in magenta.range_to(black, steps)]

    def getColor(self, count):
        '''
        This method returns a single element from the palette array at index of count
        '''
        return self.__palette[count]

