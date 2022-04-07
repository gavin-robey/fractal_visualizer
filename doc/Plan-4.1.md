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
* The output of `FractalFactory.count()`determines the color used by `PaletteFactory.getColor()`

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

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


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
