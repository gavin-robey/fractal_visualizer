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
Each will have the exact function that is described by the instructions and as described above. Also all unit tests made 
must pass in order for this project to be fully complete.

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
* The math on how this program works

## Phase 1: System Analysis *(10%)*

 **Inputs/ Data**
* Data is collected from the user from the command line using ``sys.argv``
* The data collected from the user is in the form of a list of strings, and determines which algorithm will be used.
* The name of the fractal, the fractal type as well as the fractal information is input.
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
