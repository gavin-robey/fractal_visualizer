class Palette:
    '''
    The purpose of this class is to create a blueprint of how every class implementing it must be structured.
    If the method of this class is not implemented then the program will crash with a "not implemented error"
    '''

    def getColor(self, count):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")

    def getLength(self):
        raise NotImplementedError("Concrete subclass of Palette must implement getLength() method")