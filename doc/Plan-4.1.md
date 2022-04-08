# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Description**
* This program is an interactive program that creates an image based on a given fractal algorithm.
* This program will be derived from the existing refactored code from assn4.0.
* This assignment will use polymorphism, the factory method and duck typing to achive this implementation.
* There are 4 different fractal algorithms that are acceptable. The Julia, Mandelbrot, Mandelbrot3, and Mandelbrot4 algorithms.
* There are many variations of these algorithms that will be displayed and selected by the user.
* These variations are supplied in a plethora of files in the data directory.
* Each of these files contains all the necessary configuration data such as: 
* The type of algorithm, the amount of pixels to be displayed, the center x,y coordinates, the axis length,
* the amount of iterations, and depending on the type of the algorithm, a creal, and cimag coordinate.
* This polymorphic program will have 13 modules:
* `Main.py`, `FractalFactory.py`, `FractalParser.py`, `Fractal.py`, `ImagePainter.py`, `PaletteFactory.py`, 
* `Palette.py`, 4 concrete Fractal classes, and 2 concrete Palette classes
* `Main.py` is the driver for the program, and is the only file that deals with command line arguments.
* `FractalFactory.py` is the only class that deals with the concrete classes derived from Fractal.py
* `FractalParer.py` is responsible for reading a file and determining if it is valid, if so it creates a dictionary with 
* the necessary data to build a fractal.
* `Fractal.py` is an abstract class with one method, `count()`. This is a blueprint for all concrete classes that inherit from it.
* `ImagePainter.py` is in charge of painting the image and displaying that to the screen using tkinter
* `PaletteFactory.py` is the only class that creates the concrete classes derived from Palette.py
* `Palette.py` is an abstract class with one method, `getColor()`. This is a blueprint for all concrete classes that inherit from it.

###What good solutions look like
A good solution to this project is when this program behaves according to the instructions, and incorporates all the new 
features required. This project will be complete when it behaves as expected and uses polymorphism, duck typing, and the 
factory method correctly. 

**Handling errors**
* If invalid input is used in each menu, the program will quit. 
* If a file given is invalid, then the program will crash.
* If a file given has any invalid information as determined by `FractalParser.py`, then the program will crash with the
* appropriate error message.
* If an invalid color palette is given, then the program will crash with the appropriate error message.


**What I know how to do** 
* Create classes, and modularize my code
* Create readable code.
* Use the complex function in python 
* Create loops to iterate through data
* Use the abs function in python
* read and write files
* access data from the command line

**What I need to work on/ Challenges I foresee**
* Creating Unit tests
* Understanding the math on how this program works
* Understanding abstract classes
* Using polymorphism
* Using the factory method and understanding how it works

## Phase 1: System Analysis *(10%)*


 **Inputs/ Data**
* Data is collected from the user from the command line using ``sys.argv``
* The data collected from the user is in the form of a list of strings, and determines which file will be parsed and which color palette to use.
* All fractal information is stored in a file. All information in this file is in the form of a string and
* each value must be determined if it is valid.
* This data is passed into the `FractalParser.py` which determines if the data is valid, if it is then it is input into a dictionary.
* This dictionary created from the `FractalParser.py` is input into both the `PaletteFactory.py` and the `FractalFactory.py` classes. 
* The data in this dictionary comes in the form of strings, ints, and floats.
* Depending on which algorithm or palette is selected, a list of color data will be used to determine each pixel's color in the `ImagePainter.py` class.
* This will be determined by the fractal type input data, and the selected palette 
* The coordinate of the pixel will be input into `PaletteFactory.getColor()`

**Output**
* A picture is output to the screen using Tk, Canvas, PhotoImage, and mainloop from the tkinter module.
* The picture is output using a window made from the TK class 
* Each picture contains thousands of pixels that are stored in the Canvas class
* The color of each pixel is determined by the output of `PaletteFactory.getColor()`
* Each palette is created using the output of the colour module.
* The output of `FractalFactory.count()`helps determine the color used by `PaletteFactory.getColor()`

**Algorithms**
* To determine if input is valid from the user, a check must be done, if the check fails then the program will quit 
* If not, the specified algorithm and palette will be painted.
* To paint each picture the color of each pixel will be determined.
* The color is determined by finding the amount of iterations that are needed to 
find the absolute value of the distance between a real coordinate and an imaginary coordinate
* To find the distance we can use the distance formula. 
* Then we can find the absolute value of this distance
* To find the iterations, we can loop until the right distance is found determined by the Julia algorithm,
Mandelbrot algorithm, Mandelbrot3 algorithm, or the Mandelbrot4 algorithm.



## Phase 2: Design *(30%)*
```python
in main.py
'''
This module is the main driver of the program.
This module accepts input from the user via the command line and displays a fractal picture depending on user input.
This module imports 5 modules: sys, ImagePainter, FractalParser, FractalFactory, and PaletteFactory
This module will check whether the user has not entered a file, has entered a file or has entered a file and a palette.
In each scenario, the FractalParser, FractalFactory, PaletteFactory will be called. 
Their parameters will be different depending on the scenario.
Their output will then be passed into the ImagePainter class. 
All errors will be handled in their respective classes.
'''
if default fractal, default palette:
    defaultFractal = FractalParser()
    fractalFactory = FractalFactory().makeFractal()
    paletteFactory = PaletteFactory().makePalette()
    ImagePainter(defaultFractal, fractalFactory, paletteFactory)
if not default fractal, default palette:
    chosenFractal = FractalParser(user input file)
    fractalFactory = FractalFactory().makeFractal()
    paletteFactory = PaletteFactory().makePalette()
    ImagePainter(chosenFractal, fractalFactory, paletteFactory)
if not default fractal, not default palette:
    chosenFractal = FractalParser(user input file)
    fractalFactory = FractalFactory().makeFractal()
    paletteFactory = PaletteFactory().makePalette(user input palette)
    ImagePainter(chosenFractal, fractalFactory, paletteFactory)
    
```
#### What happens with good input?
* If no arguments are passed in, then a default picture is drawn to the screen.
* If the first argument is a valid fractal file then a specified picture is drawn with the default palette
* If the first argument is a valid fractal file and the second is a valid palette, then a fractal will be drawn to the screen.
#### What happens with bad input?
* If any of the above conditions are not met then the program will crash.

#### Good Examples:
```commandline
python3 src/main.py data/starfish.frac rainbow   
```
#### Bad Examples:
```commandline
python3 src/main.py rainbow   
```

```commandline
python3 src/main.py rainbow  data/starfish.frac 
```

```commandline
python3 src/main.py data/INVALIDFILE
```

```python
in PaletteFactory.py

class PaletteFactory:
    '''
    This class imports 2 modules: Gold and Rainbow
    This class has no arguments.
    This class has one method: makePalette()
    This class has one data member: paletteName
    This class determines which palette class will be instantiated and returned. 
    This class provides a default palette unless the user selects otherwise. 
    This class returns a Palette concrete class
    '''
    def __init__():
        paletteName = default palette
  
```
#### What happens with good input?
* If this class is used correctly, then a palette object will be returned
#### What happens with bad input?
* If the makePalette() method is not called, then nothing will be returned

#### Good Examples:
```python
fractal = PaletteFactory().makePalette() 
```
#### Bad Examples:
```python
fractal = PaletteFactory()
```

```python
in PaletteFactory.py

class PaletteFactory:
    
    def makePalette(iterations, paletteName=None by default):
        '''
        Return Palette concrete class
        This method has 2 arguments: iterations and paletteName
        iterations: int: determines how large the palette needs to be
        paletteName: str: determines the palette type to be used
        This method, sets the paletteName and determines if a palette was selected then returns the specified Palette class
        If no palette was selected then a default value is used, if a palette is given, then the specified palette is used.
        If a palette is given, and it is not valid, then the program will crash and an error message will be given.
        '''
        if paletteName is not None:
            paletteName = paletteName

        if paletteName == palette type 1:
            return Palette1(iterations)
        elif paletteName == palette type 2:
            return Palette2(iterations)
        else:
            crash and give error message
```
#### What happens with good input?
* If this class is used correctly, then a palette object will be returned
#### What happens with bad input?
* If the amount of iterations is not passed into makePalette() then the program will crash
* If an invalid palette type is given then the program will crash with a NotImplemented error 

#### Good Examples:
```python
PaletteFactory().makePalette(iterations) 
```
```python
PaletteFactory().makePalette(iterations, VALIDPALETTE) 
```
#### Bad Examples:
```python
PaletteFactory().makePalette() 
```
```python
PaletteFactory().makePalette(iterations, INVALIDPALETTE) 
```

```python
in FractalFactory.py

class FractalFactory:
    '''
    This class imports 4 modules: Julia, Mandelbrot, Mandelbrot3, and Mandelbrot4
    Each of these modules are the concrete classes from Fractal.py this is the only place where they are imported.
    This class has no arguments
    This class has 2 data members: defaultFractal and configuration
    defaultFractal: dictionary of str, int, and floats: default configuration data
    configuration: initially set to defaultFractal
    This class has one method: makeFractal(): Fractal concrete class 
    This class creates a default fractal configuration dictionary, if nothing is passed in.
    Otherwise, the configuration is set to the input value.
    Then it uses this dictionary to build a Fractal concrete class and returns this class.  
    '''
    
    def __init__():
        defaultFractal = {default fractal information}
        configuration = defaultFractal
```
#### What happens with good input?
* If this class is used correctly, then a fractal object will be returned
#### What happens with bad input?
* If the makeFractal() method is not called, then nothing will be returned

#### Good Examples:
```python
fractal = FractalFactory().makeFractal() 
```
#### Bad Examples:
```python
fractal = FractalFactory()
```


```python
in FractalFactory.py

class FractalFactory:

    def makeFractal(configurationDict=None):
        '''
        Returns Fractal concrete class
        This method has one argument: configurationFile: initially set to None: can be type dictionary of int, str, and floats.
        This method finds out if a configuration Dictionary is given, if it is not then it uses the default fractal configuration
        dictionary. If a configuration dictionary is given then this is the configuration dictionary that will be used.
        Depending on the type given from this configuration dictionary, a selected Fractal class will be returned.
        '''
        if type is "typeGiven"
            return Fractal of the given type
```
#### What happens with good input?
* If this class is used correctly, then a fractal object will be returned
#### What happens with bad input?
* If invalid fractal information is passed into .makeFractal() then the program will crash

#### Good Examples:
```python
FractalFactory().makeFractal() 
```
```python
fractalInformation = FractalParser().getConfiguration()
FractalFactory().makeFractal(fractalInformation) 
```

#### Bad Examples:
```python
fractalInformation = "INVALID"
FractalFactory().makeFractal(fractalInformation) 
```

```python
in Palette.py

class Palette:
    '''
    This class is an abstract class with no arguments. 
    This class has one method: getColor().
    getColor() has one argument: count: int
    The purpose of this class is to create a blueprint of how every class implementing it must be structured.
    If the method of this class is not implemented then the program will crash with a "not implemented error"
    '''
    
     def getColor(count):
        crash and give error message if not implemented
```
#### What happens with good input?
* If all methods are used, then the program will run correctly
#### What happens with bad input?
* If this method is not implemented, then the program will crash with a NOT IMPLEMENTED ERROR

#### Good Examples:
```python
class example(Palette):
    def getColor(self, count):
```

#### Bad Examples:
```python
class example(Palette):
    def thisIsTheOnlyMethod(self):
```

```python
in Fractal.py

class Fractal:
    '''
    This class is an abstract class with no arguments. 
    This class has one method: count().
    count() has one argument: complexNumber: complex
    The purpose of this class is to create a blueprint of how every class implementing it must be structured.
    If the method of this class is not implemented then the program will crash with a "not implemented error"
    '''

    def count(complexNumber):
        crash and give error message if not implemented
```

#### What happens with good input?
* If all methods are used, then the program will run correctly
#### What happens with bad input?
* If this method is not implemented, then the program will crash with a NOT IMPLEMENTED ERROR

#### Good Examples:
```python
class example(Fractal):
    def count(self, count):
```

#### Bad Examples:
```python
class example(Fractal):
    def thisIsTheOnlyMethod(self):
```
```python
in class ImagePainter: 

    def __init__(self,fractalInformation, fractalFactory, paletteFactory):
        '''
        This class returns None, in order to draw a picture to the screen just initialize this class.
        This class has 3 arguments:
        fractalInformation: Dictionary of ints, strings and floats
        fractalFactory: FractalFactory()
        paletteFactory: PaletteFactory()
        This class has 7 data members:
        fractalInformation: Dictionary of ints, strings and floats
        fractalFactory: FractalFactory()
        paletteFactory: PaletteFactory()
        window: a window created from the tkinter module
        windowSize: Integer representing the size of the window
        img: the PhotoImage class that stores all the pixels for our image at a given size
        main: calls the main method so that this class can run without calling any methods
        This class imports 3 modules: tkinter, time, and, sys
        This class creates the picture of the specified fractal and draws it to the screen using the tkinter module.
        This class also uses the fractal information to find the distance between points and passes that data into the
        Fractal.count() method to determine the color of each pixel.
        All of these calculations are timed and the time that it takes to do these operations is printed to the console.
        '''
        fractalInformation = fractalInformation
        fractalFactory = fractalFactory
        paletteFactory = paletteFactory
        window = tkinter window
        windowSize = paletteFactory[pixels]
        img = PhotoImage(width = windowSize, height windowSize)
```
#### What happens with good input?
* If all input is correct, then a picture is drawn to the screen of a specific fractal.
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.

#### Good Examples:
```python
fractalInformation = FractalParser()
fractalFactory = FractalFactory.makeFractal()
paletteFactory = PaletteFactory.makePalette()
ImagePainter(fractalInformation, fractalFactory, paletteFactory)
```
#### Bad Examples:
```python
ImagePainter(1234, 1234, 1234)
```

```python
in class ImagePainter: 

    def __main(self):
        '''
        This method returns: None
        This method has no arguments
        This method is responsible for keeping track of the time as well as printing the time to the console, printing
        the name of the image made, saving a file containing the picture made, as well as keeping the window open.
        In between the time started, the __display() method will be called to create and display an image to the screen.
        '''
        start time
        display()
        end time

        print(total time)
        save file of picture
        print(name of picture)
        keep window open

        
        
```
#### What happens with good input?
* The functionality of this method relies on the output of the time class, and the display() method. If all the output for these classes/ methods is correct, then the method will display a fractal picture to the screen.
#### What happens with bad input?
* The functionality of this method relies on the output of the time class, and the display() method. If any of the output for these classes/methods is incorrect, then the method will not display the correct fractal to the screen, it may not even display a fractal at all, or the program will crash depending on the error of the output of the other classes/methods.

```python
in class ImagePainter: 

    def __display(self):
        '''
        This method returns: None
        This method has no arguments.
        This method finds the distance between the smallest x value, the largest x value, and the smallest y value.
        It then takes those values and finds the pixel size.
        It then creates a canvas that is the size of the window, this canvas is whats used to create an image on a window.
        This method then iterates over every row and column to input each pixel.
        In this iteration, it uses the Palette.getColor() method to determine what color the pixel is then adds this pixel to the canvas
        Then this method updates the window so all the changes to the canvas mad above are saved.
        '''
        find min x
        find max x 
        find min y 
        
        find pixel size
        
        create Canvas(window size)
        
        for row in range(window size):
            for col in range(window size):
                color = Palette.getColor(at current x and current y )
                add colored pixel to window
            update window

        
        
```
#### What happens with good input?
* The functionality of this method relies on the output of the Palette.getColor() method, the Fractal.count() method, and the tk classes. If all the output for these classes is correct, then the method will display a fractal picture to the screen.
#### What happens with bad input?
* The functionality of this method relies on the output of the Palette.getColor() mehtod, the Fractal.count() method, the tk classes. If any of the output for these classes is incorrect, then the method will not display the correct fractal to the screen, it may not even display a fractal at all, or the program will crash depending on the error of the output of the other classes/methods.

#### Good Examples:
```python
color = Palette.getColor(Fractal.count(at current x and current y ))
color = is valid color
```
#### Bad Examples:
```python
color = Palette.getColor(Fractal.count(at current x and current y ))
color = is not valid color
```
```python
color = Palette.getColor(Fractal.count(at current x and current y ))
color = PalettegetColor failed and program crashed
```

```python
in Julia.py, Mandelbrot.py, Mandelbrot3.py, or Mandelbrot4.py
'''(strictly for readability sake I will document all of these files in this one section. They are all built exactly the same
but have a few minor differences)'''

class anyOfTheNamesAbove(Fractal):
    '''
    Return: int
    This class imports one module: Fractal
    This class has one method: count()
    This class has one argument: iterations: int: determines how many times the main loop must be executed
    This class applies the algorithms of all the types above.
    '''
    
    def __init__(iterations):
        iterations = iterations
    
    @Override
    def count(z or c):
        '''
        This function returns: Integer
        This function has 1 argument:
        z or c: Complex
        This function loops through the length of the color palette and depending on some magic from the julia, mendelbrot, etc algorithms
        it returns the number of iterations
        '''
        c = complex at (-1,0) "(for julia) otherwise" 
        z = complex at (0,0 ) "(for mandelbrots)"
        for length of iterations:
            (z = z * z + c ) "(Julia algorithm) otherwise it will be whatever algorithm is being used"
            if absolute value of z or c  > 2:
                add to count 
                return count
```
#### What happens with good input?
* If all input is correct, then the number of iterations as determined by the respective algorithm is output
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* The `z or c` argument must be a complex number
* For example, if `c or z` is not a complex number, then the program will crash with an `incompatable type` error
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
count(complex(1,2))
```
#### Bad Examples:
```python
count(1)
```
```python
count()
```

```python
in Gold.py or Rainbow.py
'''(strictly for readability sake I will document all of these files in one document. They are all built exactly the same
but have a few minor differences)'''

class anyOfTheNamesAbove(Palette):
    '''
    Return: str
    This class imports 3 modules: Palette, colour, and math
    This class has one argument: iterations
    iterations: int: determines how large the palette will be
    This class has 2 data members: iterations and palette
    iterations: int
    palette: array of strings: contains the list od colors to be used in the program 
    This class creates a color palette, then returns a single color from this color palette
    It does this by using the colour module, and appending a range of colors from one value to another.
    For more variation multiple colors are given and multiple ranges are set. 
    Each range is added to the palette array.
    Each range is in a loop that runs to the length of 'iterations' 
    '''

    def __init__(iterations):
        iterations = iterations
        palette = []
        for i in range iterations:
            palette = white range to blue
            palette += blue range to red
            
    def getColor(count):
        '''
        Return: str
        This method has one argument: count: int
        This method returns a single element from the palette array at index of count
        '''
        return palette at count
```
#### What happens with good input?
* If all input is correct, then a single color is output.
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if `count` is not an integer number, then the program will crash.
* The `iterations` argument must be an integer
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
Gold(512).getColor(0)
```
#### Bad Examples:
```python
Gold("512").getColor(complex(1,2))
```
```python
Gold().getColor()
```

```python
in FractalParser.py

class FractalParser:
    '''
    Return: dictionary of str, int, and floats
    This class imports no modules
    This class has one argument: fileName: the given file from the user
    This class has 3 data members: 
    configuration: dictionary of str, int, and floats
    shouldContain: array of strings
    configurationTypes: dictionary of str, int, and floats
    This class has 6 methods: 
    getConfiguration(): return configuration
    verify(): void: verifies the dictionary is valid
    checkMissing(): void: ensures no items are missing
    missingItems(): array of strings: helper method for checkMissing
    checkTypes(): void: checks to ensure the types for each item are correct 
    isFloat(): Boolean: checks if an item is a float
    This class reads a file given to it and ensures that the file contains all the 
    necessary items, has the correct types, that each item has a value, and places all this 
    data into a dictionary to be used later
    '''

    def __init__(self, fileName):
        configuration = {}
        shouldContain = [all keys that must be present in the file]
        configurationTypes = {dictionary that stores all the needed types}
        
```
#### What happens with good input?
* If this class is used correctly, then a formatted dictionary  will be returned
#### What happens with bad input?
* If the .getConfiguration() method is not called, then nothing will be returned
* If the file is not passed in, then the program will crash
* If the file is not valid, then the program will crash
* If the contents of the file are not valid, then the program will crash.

#### Good Examples:
```python
fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
```
#### Bad Examples:
```python
fractalInformation = FractalParser().getConfiguration()
```
```python
fractalInformation = FractalParser()
```
```python
fractalInformation = FractalParser(NOT_A_VALID_FILE).getConfiguration()
```
```python
fractalInformation = FractalParser(CONTENTS_ARE_INVALID).getConfiguration()
```

```python
in FractalParser.py

class FractalParser:
    
    def getConfiguration():
        '''
        Returns: dictionary of ints, strs, and floats
        This method has no arguments 
        This method calls verify() to ensure that the dictionary is valid
        Then it returns the configuration dictionary
        '''
        verify()
        return configuration
```
#### What happens with good input?
* If this file given is completely correct, then a formatted dictionary  will be returned
#### What happens with bad input?
* If the contents of the file are not valid, then the program will crash.
* If there are missing elements then the porgram will crash
* If there are extra values, then the program will crash
* If there are invalid types then the program will crash

#### Good Examples:
```python
fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
```
#### Bad Examples:
```python
fractalInformation = FractalParser(NOT_A_VALID_FILE).getConfiguration()
```
```python
fractalInformation = FractalParser(CONTENTS_ARE_INVALID).getConfiguration()
```

```python
in FractalParser.py

class FractalParser:
    
    def verify():
        '''
        Return None
        this method has no arguments
        This method checks if the 'type' key is in the dictionary, if it is 
        then call checkMissing() and checkTypes()
        If it is not then raise a RuntimeError
        '''
        if 'type' is not in configuration:
            checkMissing()
            checkTypes()
        else:
            raise RuntimeError
```
#### What happens with good input?
* If this file given is completely correct, then no errors will be raised
#### What happens with bad input?
* If the contents of the file are not valid, then the program will crash.
* If there are missing elements then the porgram will crash
* If there are extra values, then the program will crash
* If there are invalid types then the program will crash

#### Good Examples:
```python
sys.arv[1] is valid
fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
```
#### Bad Examples:
```python
fractalInformation = FractalParser(NOT_A_VALID_FILE).getConfiguration()
```
```python
fractalInformation = FractalParser(CONTENTS_ARE_INVALID).getConfiguration()
```

```python
in FractalParser.py

class FractalParser:
    
    def checkMissing():
        '''
        Return None 
        This method has no arguments 
        This method checks the type of the fractal that is being accessed
        Then check if the dictionary contains any missing items using the missingItems() method
        If there are missing items, then a runtime error will be raised
        If the item we are checking happens to be a mandelbrot fractal, then 
        check if there are "creal" or "cimag" items involved. If there are then
        raise a Runtime error
        '''
        if fractalType = julia:
            if items are missing
                raise Runtime error
        if  fractalType is  mandelbrot:
            if items are missing 
                raise Runtime error
            if contains "creal" or "cimag"
                raise Runtime error
        if wrong type is given:
            raise runtime error
                
            
```
#### What happens with good input?
* If this file given is completely correct, then no errors will be raised
#### What happens with bad input?
* If the contents of the file are not valid, then the program will crash.
* If there are missing elements then the porgram will crash
* If there are extra values, then the program will crash
* If there are invalid types then the program will crash

#### Good Examples:
```python
sys.arv[1] is valid
fractalInformation = FractalParser(sys.argv[1]).getConfiguration()
```
#### Bad Examples:
```python
fractalInformation = FractalParser(NOT_A_VALID_FILE).getConfiguration()
```
```python
fractalInformation = FractalParser(CONTENTS_ARE_INVALID).getConfiguration()
```

```python
in FractalParser.py

class FractalParser:
    
    def missingItems():
        '''
        Return array of strings 
        This method has no arguments
        This method checks if there are any items that are not in the configuration dictionary
        If there are missing items then the missing items are appended to an array and returned 
        This is done so that we can access the items that are missing and alert the 
        user which items are missing.
        '''
        itemsMissing = []
        if item in shouldContain is not in configuration:
            itemsMissing.append(item)
        return itemsMissing
```
#### What happens with good input?
* If there are no missing items, then an empty array will be returned
#### What happens with bad input?
* If there are missing items then they will be appended to the array and returned

#### Good Examples:
```python
if len(missingItems()) == 0:
    return IS_RETURNED
```
#### Bad Examples:
```python
if len(missingItems()) == 0:
    return IS_NOT_RETURNED
```

```python
in FractalParser.py

class FractalParser:
    
    def checkTypes():
        '''
        Return None 
        This method has no arguments 
        This method checks the types of the elements in the configuration by 
        looping through the configuration and checking to ensure the types match.
        If there is an item missing then raise a Runtime error
        '''
        for item in configuration:
            if item is not the right type:
                raise runtime error
```
#### What happens with good input?
* If all types are valid, then no errors will be raised
#### What happens with bad input?
* If any of the types from the dictionary are not correct, then an error will be raised.

#### Good Examples:
```python
if checkTypes() == "does not raise an error":
    return "dictionary is correct"
```
#### Bad Examples:
```python
if checkTypes() == "raise an error":
    return "dictionary has incorrect types"
```
```python
in FractalParser.py

class FractalParser:
    
    def isFloat(val):
        '''
        Return Boolean 
        This method has 1 argument: val: can be any type
        This method uses a try catch block then tests if an item passed in is actually a float
        I got the implementation of this technique from https://www.programiz.com/python-programming/examples/check-string-number
        '''
        try: 
            if val is a float
            return true
        except valueError:
            return false
```
#### What happens with good input?
* There is no good or bad input, the purpose of this method is to never crash no matter what types are passed in
#### What happens with bad input?
* There is no good or bad input, the purpose of this method is to never crash no matter what types are passed in


## Phase 3: Implementation *(15%)*

I had a weird infinite loop glitch it was pretty weird, but I fixed it.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
