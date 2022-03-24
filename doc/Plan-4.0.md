# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Description**
* This program is an interactive program that creates an image based on a fractal algorithm.
* There are two different types of fractal algorithms, the Julia algorithm and the Mandelbrot algorithm.
* There are many variations of these algorithms that will be displayed and selected by the user.
* The implementation of the functionality described above is already complete but is completed by extremely messy code.
* The current implementation must be refactored to be readable.
* Unused code can be deleted, parameters can be changed, function and variable names can be changed, and redundant code should be deleted.
* The refactored code must be split into 6 different modules: 
* Main.py, FractalInformation.py, ImagePainter.py, Julia.py, Mandelbrot.py, and Palette.py 
* Main.py is the driver for the program, and is the only file that deals with command line arguments.
* FractalInformation.py stores all the information to make a fractal in a dictionary
* ImagePainter.py is in charge of painting the image and displaying that to the screen
* Palette.py contains the color palette for both algorithm types, and returns the color for a specific pixel.
* Julia.py returns the number of iterations found using the Julia algorithm
* Mandelbrot.py returns the number of iterations found using the Mandelbrot algorithm
* At the end of this project, this code should display the exact same output as the original program but will be organized.

###What good solutions look like
A good solution to this project is when this program is written completely differently but outputs the exact same thing
as the original implementation. This project will be complete when all 6 modules are written in a clean and concise manner.
Each will have the exact function that is described by the instructions as described above. Also, 7 unit tests must be 
altered or created and must pass in order for this project to be fully complete.

**Handling errors**
* If invalid input is used in each menu, the program will quit

**What I know how to do** 
* Create classes, and modularize my code
* Create readable code.
* Use the complex function in python 
* Create loops to iterate through data
* Use the abs function in python

**What I need to work on/ Challenges I foresee**
* Reading other people's code
* Creating Unit tests
* Understanding the math on how this program works

## Phase 1: System Analysis *(10%)*

 **Inputs/ Data**
* Data is collected from the user from the command line using ``sys.argv``
* The data collected from the user is in the form of a list of strings, and determines which algorithm will be used.
* The name of the fractal, the fractal type as well as the fractal information is input using the information gained from the user.
* A coordinate is input into the Palette class.
* Depending on which algorithm is selected, a list of color data will be used to determine each pixel's color in the Palette class.
* This will be determined by the fractal type input data 
* In both the Julia and Mandelbrot module, the coordinate of the pixel as well as the length of the color data will be input

**Output**
* A picture is output to the screen using Tk, Canvas, PhotoImage, and mainloop from the tkinter module.
* The picture is output using a window made from the TK class 
* Each picture contains thousands of pixels that are stored in the Canvas class
* The color of each pixel is determined by the output of the Palette class
* The output of the Julia and Mandelbrot files determines the color used by the Palette class

**Algorithms**
* To determine if input is valid from the user, a check must be done, if the check fails then the program will quit 
* If not, the specified algorithm will be painted.
* To paint each picture the color of each pixel will be determined.
* The color is determined by finding the amount of iterations that are needed to 
find the absolute value of the distance between a real coordinate and an imaginary coordinate
* To find the distance we can use the distance formula. 
* Then we can find the absolute value of this distance
* To find the iterations, we can loop until the right distance is found determined by either the Julia algorithm or the 
Mandelbrot algorithm.


## Phase 2: Design *(30%)*

```python
in main.py
'''
This module is the main driver of the program.
This module accepts input from the user via the command line and displays a fractal picture depending on user input.
This module imports 3 modules: sys, ImagePainter, and FractalInformation
Most of this file will be very simular to the starter code, the only things to change will be which modules are used to 
output the picture.
All of the commands for either the Julia algorithm or the Mandelbrot algorithm are stored in a list.
This is done to check if the given command is valid.
If there are no arguments given, then the program will display all the fractal types the user can enter and exit.
If there is an argument that is passed in, but it is not valid then an error message will display, all the fractal types will be displayed
and the program will exit.
If there is an argument that is passed in, and it is valid, then the appropriate algorithm will be used.
This will be achieved by calling the ImagePainter class and passing in the fractal information and the fractal type
'''
JULIAS = [ julia algorithm variations]
MBROTS = [ Mandelbrot algorithm variations]
	         	  
if no arguments:  	         	  	         	  
    for fractal in all fractal types:  	         	  
        print(fractal)
    exit()

if invalid argument:  	         	  
    print("error message")  	         	  
    for fractal in all fractal types:
        print(fractal)  	         	  
    exit()
else:
    if argument is JULIAS:
        ImagePainter(fractals from FractalInformation, fractal type)
    elif argument is MBROTS:
        ImagePainter(fractals from FractalInformation, fractal type)
```
#### What happens with good input?
* If no arguments are given, then the program outputs the fractal types to the console
* If a valid argument is given, a selected fractal type picture is drawn to the screen.
#### What happens with bad input?
* If an invalid argument is given, then the program prints an error message to the console, displays the fractal types, and exits the program.
* If more than one argument is given, then the first given argument is used to draw the picture.
* Obviously if an invalid path is given when initially running this program, then an invalid path error will occur

#### Good Examples:
```commandline
 python3 src/main.py     
```
```commandline
python3 src/main.py fulljulia
```
#### Bad Examples:
```commandline
 python3 src/main.py INVALIDTYPE
```
```commandline
 python3 src/main.py fulljulia hourglass
```
```commandline
 python3 main.py
```

```python
in FractalInformation.py
'''
This module contains all the needed information for each fractal
This module consists of only one dictionary containing all the values used.
There are 12 keys each containing necessary values. 
Each of the 12 keys contains another dictionary that holds 3 keys each.
These keys are 'centerX', 'centerY', and 'axisLen'
'''
# This pattern will be repeated for the 12 values
fractals = {fractalType: x: data, y: data, axisLen: data }

```
#### What happens with good input?
* There is no input with this file, only an outputted dictionary
#### What happens with bad input?
* There is no input with this file, only an outputted dictionary

```python
in class ImagePainter 

    def __init__(self, imageName, fractalInformation, fractalType):
        '''
        This class returns None, in order to draw a picture to the screen just initialize this class.
        This class has 3 arguments:
        imageName: String 
        fractalInformation: Dictionary with keys of type String and values of type Integer
        fractalType: String 
        This class has 7 data members:
        imageName: String 
        fractal: Dictionary with keys of type String and values of type Integer
        fractalType: String 
        window: a window created from the tkinter module
        windowSize: Integer representing the size of the window
        img: the PhotoImage class that stores all the pixels for our image at a given size 
        main: calls the main method so that this class can run without calling any methods
        This class imports 4 modules: tkinter, time, Palette, and sys
        This class creates the picture of the specified fractal and draws it to the screen using the tkinter module.
        This class also uses the fractal information to find the distance between points and passes that data into the 
        Palette class to determine the color of each pixel.
        All of these calculations are timed and the time that it takes to do these operations is printed to the console.
        '''
        imageName = imageName
        fractal = fractalInformation at imageName
        fractalType = fractalType
        window = tkinter window
        windowSize = 512
        img = PhotoImage(width = windowSize, height windowSize)
```
#### What happens with good input?
* If all input is correct, then a picture is drawn to the screen of a specific fractal.
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if imageName is an integer, then it will be considered the wrong key and the program will get a `KeyError:`
* The fractalInformation argument must be a dictionary
* If all of the arguments are not given then the program will crash

#### Good Examples:
```python
ImagePainter("imageName", fractalDictionary, "fractalType")
```
#### Bad Examples:
```python
ImagePainter(1234, notADictionary, 1234)
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
        In this iteration, it uses the Palette class to determine what color the pixel is then adds this pixel to the canvas
        Then this method updates the window so all the changes to the canvas mad above are saved.
        '''
        find min x
        find max x 
        find min y 
        
        find pixel size
        
        create Canvas(window size)
        
        for row in range(window size):
            for col in range(window size):
                color = Palette(at current x and current y )
                add colored pixel to window
            update window

        
        
```
#### What happens with good input?
* The functionality of this method relies on the output of the Palette class, and the tk classes. If all the output for these classes is correct, then the method will display a fractal picture to the screen.
#### What happens with bad input?
* The functionality of this method relies on the output of the Palette class, and the tk classes. If any of the output for these classes is incorrect, then the method will not display the correct fractal to the screen, it may not even display a fractal at all, or the program will crash depending on the error of the output of the other classes/methods.

#### Good Examples:
```python
color = Palette(at current x and current y )
color = is valid color
```
#### Bad Examples:
```python
color = Palette(at current x and current y )
color = is not valid color
```
```python
color = Palette(at current x and current y )
color = Palette failed and program crashed
```
```python
in class Palette: 

    def __init__(self, fractalType, coordinate):
        '''
        This class returns String, more specifically a string representing a color.
        This class has 2 arguments:
        fractalType: String
        coordinate: Complex number
        This class has 4 data members: 
        fractalType: String: representing the type of the fractal
        coordinate: Complex: representing the coordinate of the real and imaginary number
        mbrotPalette: List of Strings: Representing the color palette for the mandelbrot algorithm
        juliaPalette: List of Strings: Representing the color palette for the julia algorithm
        This class returns the color of the current pixel by finding the index of the specific color palette given 
        by either the Mandelbrot module or the Julia module.
        '''
        fractalType 
        coordinate
        mbrotPalette[All colors used]
        juliaPalette[All colors used]
```
#### What happens with good input?
* If all input is correct, then a string representing a color is returned
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if fractalType is an integer, then the program will crash with an `incompatable type` error
* The fractalInformation argument must be a complex number
* If all the arguments are not given then the program will crash

#### Good Examples:
```python
Palette("julia", complex(1,2))
```
#### Bad Examples:
```python
Palette("NotAType", 1)
```
```python
Palette(1, 1)
```

```python
in class Palette:
    def getPixeColor(self):
        '''
        This method returns: String
        This method has no arguments
        This method checks which type of fractal is being called
        Then it returns a color from the proper color palette by using the index returned by either the Julia or Mandelbrot 
        modules.
        '''

        if type is julia:
            return colorPalette[index from Julia]
        if type is Mandelbrot:
            return colorPalette[index from Mandelbrot]
```

#### What happens with good input?
* The functionality of this method relies on the output of either the Julia module or the Mandelbrot module, if these outputs are correct, then a single color string will be output.
#### What happens with bad input?
*  The functionality of this method relies on the output of either the Julia module or the Mandelbrot module, if these outputs are not correct, depending on their output, the program could be using the wrong color or the program could experience an `out of bounds ` error.

#### Good Examples:
```python
colorPalette[index is in range and correct]
```
#### Bad Examples:
```python
colorPalette[index is in range but not correct]
```
```python
colorPalette[index is out of range and not correct]
```
```python
in Julia.py

def getCount(z, paletteLength):
    '''
    This function returns: Integer
    This function has 2 arguments:
    z: Complex
    paletteLength: Integer
    This function loops through the length of the color palette and depending on some magic from the julia algorithm
    it returns the number of iterations
    (the pseudo code below is something I don't quite understand because I don't know how the julia algorithm works)
    '''
    c = complex at (-1,0)
    for length of paletteLength:
        z = z * z + c #This part I don't understand
        if absolute value of z  > 2:
            add to count 
            return count
    
```

#### What happens with good input?
* If all input is correct, then the number of iterations as determined by the Julia algorithm is output
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if `paletteLength` is not an integer, then the program will crash with an `incompatable type` error
* The `z` argument must be a complex number
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
getCount(complex(1,2), 5)
```
#### Bad Examples:
```python
getCount(1, "Five")
```

```python
in Mandelbrot.py

def getCount(z, paletteLength):
    '''
    This function returns: Integer
    This function has 2 arguments:
    z: Complex
    paletteLength: Integer
    This function loops through the length of the color palette and depending on some magic from the mandelbrot algorithm
    it returns the number of iterations
    (the pseudo code below is something I don't quite understand because I don't know how the mandelbrot algorithm works)
    '''
    c = complex at (0,0)
    for length of paletteLength:
        c = c * c + z #This part I don't understand
        if absolute value of z  > 2:
            add to count 
            return count
    
```

#### What happens with good input?
* If all input is correct, then the number of iterations as determined by the Mandelbrot algorithm is output
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if `paletteLength` is not an integer, then the program will crash with an `incompatable type` error
* The `z` argument must be a complex number
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
getCount(complex(1,2), 5)
```
#### Bad Examples:
```python
getCount(1, "Five")
```


## Phase 3: Implementation *(15%)*

* This project was awesome, it was nice not having to fully solve the problem that this code is doing, but rather, 
focus on the structure and the way my code works together. I had a lot of fun doing it and i'm excited to add more features!


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
