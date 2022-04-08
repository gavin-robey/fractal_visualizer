class Fractal:
    '''
    The purpose of this class is to create a blueprint of how every class implementing it must be structured.
    If the method of this class is not implemented then the program will crash with a "not implemented error"
    '''

    def count(self, complexNumber):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

