from Gold import Gold
from Rainbow import Rainbow


class PaletteFactory:
    '''
    This class determines which palette class will be instantiated and returned.
    This class provides a default palette unless the user selects otherwise.
    This class returns a Palette concrete class
    '''

    def __init__(self):
        self.paletteName = "gold"


    def makePalette(self, iterations, paletteName=None):
        '''
        This method, sets the paletteName and determines if a palette was selected then returns the specified Palette class
        If no palette was selected then a default value is used, if a palette is given, then the specified palette is used.
        If a palette is given, and it is not valid, then the program will crash and an error message will be given.
        '''
        if paletteName is not None:
            self.paletteName = paletteName

        if self.paletteName == "gold":
            return Gold(iterations)
        elif self.paletteName == "rainbow":
            return Rainbow(iterations)
        else:
            raise NotImplementedError("Invalid palette requested")