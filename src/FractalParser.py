class FractalParser:
    '''
    This class reads a file given to it and ensures that the file contains all the
    necessary items, has the correct types, that each item has a value, and places this
    data into a dictionary to be used later
    '''

    def __init__(self, fileName):
        self.__configuration = {}
        self.__shouldContain = ["type", "pixels", "centerx", "centery", "axislength", "iterations", "creal", "cimag", "name"]
        self.__configurationTypes = {"type": str, "pixels": int, "centerx": float, "centery": float, "axislength": float, "iterations": int, "creal": float,  "cimag": float, "name": str}
        name = fileName.replace("data/", "")  # remove this line until testing is done, if this is not here, then all files in data will be overridden
        self.__configuration["name"] = name.replace(".frac", "")
        file = open(fileName)
        for line in file.readlines():
            key = line.lower().strip().split(":")
            if "#" not in key[0] and key[0] in self.__shouldContain:
                if key[1].strip().isdigit() and key[0] != "creal" and key[0] != "cimag":
                    self.__configuration[key[0]] = int(key[1])
                elif self.__isFloat(key[1]) or key[0] == "creal" or key[0] == "cimag":
                    self.__configuration[key[0]] = float(key[1])
                else:
                    self.__configuration[key[0]] = key[1].strip()
        file.close()

    def getConfiguration(self):
        '''
        This method calls verify() to ensure that the dictionary is valid
        Then it returns the configuration dictionary
        '''
        self.__verify()
        return self.__configuration

    def __verify(self):
        '''
        This method checks if the 'type' key is in the dictionary, if it is
        then call checkMissing() and checkTypes()
        If it is not then raise a RuntimeError
        '''
        if 'type' in self.__configuration:
            self.__checkMissing()
            self.__checkTypes()
        else:
            raise RuntimeError("The 'type' parameter is missing")

    def __checkMissing(self):
        '''
        This method checks the type of the fractal that is being accessed
        Then checks if the dictionary contains any missing items using the missingItems() method
        If there are missing items, then a runtime error will be raised
        If the item we are checking happens to be a mandelbrot fractal, then
        check if there are "creal" or "cimag" items involved. If there are then
        raise a Runtime error
        '''
        fractalType = self.__configuration['type']
        if fractalType == "julia":
            if len(self.__missingItems()) > 0:
                raise RuntimeError(f"The required parameter '{self.__missingItems()[0]}' is missing")
        elif fractalType == "mandelbrot" or fractalType == "mandelbrot3" or fractalType == "mandelbrot4":
            if "creal" not in self.__missingItems() or "cimag" not in self.__missingItems():
                raise RuntimeError(f"This is a Mandelbrot fractal, the 'creal' and 'cimag' parameters are prohibited")
            elif len(self.__missingItems()) > 2 and "creal" in self.__missingItems() or len(
                    self.__missingItems()) > 2 and "cimag" in self.__missingItems():
                raise RuntimeError(f"The required parameter '{self.__missingItems()[0]}' is missing")
        else:
            raise RuntimeError(f"A file with a proper type must be given. {fractalType} is not a valid type")

    def __missingItems(self):
        '''
        This method checks if there are any items that are not in the configuration dictionary
        If there are missing items then the missing items are appended to an array and returned
        This is done so that we can access the items that are missing and alert the
        user which items are missing.
        '''
        itemsMissing = []
        for item in self.__shouldContain:
            if item not in self.__configuration:
                itemsMissing.append(item)
        return itemsMissing

    def __checkTypes(self):
        '''
        This method checks the types of the elements in the configuration by
        looping through the configuration and checking to ensure the types match.
        If there is an item missing then raise a Runtime error
        '''
        for key in self.__configuration:
            if self.__configuration[key] == "":
                raise RuntimeError(f"The value of the {key} parameter is missing")
            elif type(self.__configuration[key]) != self.__configurationTypes[key]:
                raise RuntimeError(f"The value of the {key} parameter is not a {str(self.__configurationTypes[key])}")

    def __isFloat(self, val):
        '''
        This method uses a try catch block then tests if an item passed in is actually a float
        I got the implementation of this technique from:
        https://www.programiz.com/python-programming/examples/check-string-number
        '''
        try:
            float(val)
            return True
        except ValueError:
            return False