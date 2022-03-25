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
Each of the 12 keys contains another dictionary that holds 4 keys each.
These keys are 'centerX', 'centerY', 'axisLen', and 'type'
'''
# This pattern will be repeated for the 12 values
fractals = {fractalType: x: data, y: data, axisLen: data, type: fractalType}

```
#### What happens with good input?
* There is no input with this file, only an outputted dictionary
#### What happens with bad input?
* There is no input with this file, only an outputted dictionary

```python
in class ImagePainter: 

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
        This class imports 6 modules: tkinter, time, Palette, sys, Julia and Mandelbrot
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

    def __init__(self, fractalType, coordinate, julia, mbrot):
        '''
        This class returns String, more specifically a string representing a color.
        This class has 4 arguments:
        fractalType: String
        coordinate: Complex number
        julia: Julia module
        mbrot: Mandelbrot module
        This class has 6 data members: 
        fractalType: String: representing the type of the fractal
        coordinate: Complex: representing the coordinate of the real and imaginary number
        julia: Julia module: represents the julia module and all its data
        mbrot: Mandelbrot module: represents the mandelbrot module and al its data
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
in class Palette:
    def __len__(self):
        '''
        returns: Integer 
        This method has no arguments
        This method returns the length of the selected palette
        It does this by checking the type and then returning the length of the correct type of palette
        '''
        if type is julia:
            return len(julia palette)
        elif type is mandelbrot:
            return len(mandelbrot palette)
```
#### What happens with good input?
* The functionality of this method relies on the existence of either the julia or mandelbrot color palette lists, if these exist then there will be no errors.
#### What happens with bad input?
* The functionality of this method relies on the existence of either the julia or mandelbrot color palette lists, if these do not exist then there will be errors.

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
getCount()
```

```python
in Julia.py

def testPixelAmount(row, col):
    '''
    This function returns: Integer
    This function has 2 arguments:
    row: Integer
    col: Integer
    This function returns the amount of pixels created depending on a row or column amount
    This function is used for the purposes of unit testing.
    '''
    return row * col
    
```
#### What happens with good input?
* If all input is correct, then the number of pixels created is output
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if `col` is not an integer, then the program will crash with an `incompatable type` error
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
testPixelAmount(1,2)
```
#### Bad Examples:
```python
testPixelAmount("five",2)
```
```python
testPixelAmount()
```


```python
in Mandelbrot.py

def getCount(c, paletteLength):
    '''
    This function returns: Integer
    This function has 2 arguments:
    c: Complex
    paletteLength: Integer
    This function loops through the length of the color palette and depending on some magic from the mandelbrot algorithm
    it returns the number of iterations
    (the pseudo code below is something I don't quite understand because I don't know how the mandelbrot algorithm works)
    '''
    z = complex at (0,0)
    for length of paletteLength:
        z = z * z + c #This part I don't understand
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
```python
getCount()
```

```python
in Mandelbrot.py

def testPixelAmount(row, col):
    '''
    This function returns: Integer
    This function has 2 arguments:
    row: Integer
    col: Integer
    This function returns the amount of pixels created depending on a row or column amount
    This function is used for the purposes of unit testing.
    '''
    return row * col
    
```
#### What happens with good input?
* If all input is correct, then the number of pixels created is output
#### What happens with bad input?
* If any of the arguments are the wrong type then the program will crash.
* For example, if `col` is not an integer, then the program will crash with an `incompatable type` error
* If any of the arguments are not given then the program will crash

#### Good Examples:
```python
testPixelAmount(1,2)
```
#### Bad Examples:
```python
testPixelAmount("five",2)
```
```python
testPixelAmount()
```



## Phase 3: Implementation *(15%)*

* This project was awesome, it was nice not having to fully solve the problem that this code is doing, but rather, 
focus on the structure and the way my code works together. I had a lot of fun doing it and i'm excited to add more features!


## Phase 4: Testing & Debugging *(30%)*

&nbsp; **Error**


&nbsp;&nbsp; When running the program and trying to run `python src/main.py fulljulia` I got this error:
```commandline
src/main.py fulljulia
Traceback (most recent call last):
  File "/Users/gavinrobey/cs1440-robey-gavin-assn4/src/main.py", line 58, in <module>
    julia.julia_main(sys.argv[1])  	         	  
  File "/Users/gavinrobey/cs1440-robey-gavin-assn4/src/julia_fractal.py", line 149, in julia_main
    makePictureOfFractal(images, image, ".png", window, juliaPalette, img, GREY0, 512)
  File "/Users/gavinrobey/cs1440-robey-gavin-assn4/src/julia_fractal.py", line 46, in makePictureOfFractal
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
KeyError: 'axisLen'
```

&nbsp; **Solution**

&nbsp;&nbsp; The reason this happened was because when unifying the way both programs were written, I copied the implementation of how the fractal information was being accessed from the Mandelbrot implementation but in the julia code, it uses the term length not len. This Is why there was a crash.


&nbsp; **Error**

&nbsp;&nbsp; When running the program I got this error:
```commandline
gavinrobey@Gavins-MacBook-Air cs1440-robey-gavin-assn4 % python3 src/main.py mandelbrot
\Traceback (most recent call last):
  File "/Users/gavinrobey/cs1440-robey-gavin-assn4/src/main.py", line 59, in <module>
    imagePainter = ImagePainter(fractalName, fractals, "mbrot")
TypeError: ImagePainter() takes no arguments
gavinrobey@Gavins-MacBook-Air cs1440-robey-gavin-assn4 % \
```

&nbsp; **Solution**

&nbsp;&nbsp; I had this error because I was an idiot and instead of creating an initializer I created __int__() instead so this happened. This was obviously an easy fix, but crazy how one dumb letter can cause alot of frustration.


&nbsp; **Error**

&nbsp;&nbsp; When running the program I got this error:



![](../data/assn4-0_failure.png)


&nbsp; **Solution**

&nbsp;&nbsp; All of my output pictures had the wrong colors in the wrong spots
This was because I forgot to subtract one from the total count, my colors were off because we are using this as an index, so there will be off by one error. After fixing this issue, the output looked correct.


&nbsp; **Error**

&nbsp;&nbsp; When running the first Julia unit test I got this error:
```commandline
Ran 1 test in 0.002s

FAILED (failures=1)


#009cb3 != #002277

Expected :#002277
Actual   :#009cb3
```
&nbsp; **Solution**

&nbsp;&nbsp; It turns out I fell for a lying comment in the original code. I picked up that the comment was lying in my code smells
document, the comment was saying that the number of iterations of the julia color palette was 76, then it inputted 78. Well turns out 
neither of these values are the length of the Julia color palette, it was actually 96. The porgram did not need the last 18 values, but then the last output was
the last value of the array. This means that the last color was wrong and this is why my unit test was failing. I did not 
even notice that the output color of my refactored program was different until I compared against the old one and tested my code.


&nbsp; **Running Unit Tests**

&nbsp;&nbsp; After fixing the one error above, these were the results of my unit tests:
```commandline
gavinrobey@Gavins-MacBook-Air cs1440-robey-gavin-assn4 % python3 src/runTests.py
testNumOfFractals (Testing.TestMandelbrot.TestMandelbrot) ... ok
testPixelAmount (Testing.TestMandelbrot.TestMandelbrot) ... ok
test_colorOfThePixel (Testing.TestMandelbrot.TestMandelbrot) ... ok
test_palleteLength (Testing.TestMandelbrot.TestMandelbrot) ... ok
testAxisLength (Testing.TestJulia.TestJulia) ... ok
testNumOfFractals (Testing.TestJulia.TestJulia) ... ok
testPixelAmount (Testing.TestJulia.TestJulia) ... ok
test_colorOfThePixel (Testing.TestJulia.TestJulia) ... ok
test_palleteLength (Testing.TestJulia.TestJulia) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

&nbsp; **What these tests mean**

&nbsp;&nbsp; I have 9 tests total: 

testNumOfFractal: This tests how many fractal types are in the dictionary

testPixelAmount: This tests to ensure the pixel amount is what it should be

test_colorOfThePixel: This tests that a specific pixel is the right color 

test_paletteLength: This tests to ensure that the color palette has the correct length 

testAxisLength: This tests to make sure both the dictionary can be accessed properly but also so that the axis length is correct 

(All data was contrived from the original starter code, all tests pass on the standards of output from the starter code)




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


*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
    * *I think this is some of the cleaner code ive written, but I do think the image painter class could be much cleaner*
        * Are there parts of your program which you aren't quite sure how/why they work?
        * *Yeah I still have no idea how the julia or mandelbrot algorithms work but thats ok I understand my code*
        * If a bug is reported in a few months, how long would it take you to find the cause?
        * *It would not take long at all*
    * Will your documentation make sense to...
        * ...anybody besides yourself?
        * *Hopefully*
        * ...yourself in six month's time?
        * *Yes I would be able to*
    * How easy will it be to add a new feature to this program in a year?
    * *Pretty easy, this was the purpose of this project after all*
    * Will your program continue to work after upgrading...
        * ...your computer's hardware?
        * *Yes*
        * ...the operating system?
        * *Yes*
        * ...to the next version of Python?
        * *Yes*
*   Fill out the Assignment Reflection on Canvas.
