# CS 1440 Assignment 4: Refactoring & Design Patterns

## 4.0: Refactoring
*   [Instructions](./instructions/README-4.0.md)
    *   [Tkinter Installation & Troubleshooting](./instructions/Tkinter.md)
*   [Hints](./instructions/Hints-4.0.md)
*   [Rubric](./instructions/Rubric-4.0.md)


## 4.1: Design Patterns
* [Instructions](./instructions/README-4.1.md)
* [Hints](./instructions/Hints-4.1.md)
* [Rubric](./instructions/Rubric-4.1.md)
* The [Fractal Gallery](./data/README.md)

## To whoever is grading this assignment:
* The unit tests need to be run in the root directory.
* The reason this needs to happen is because I'm testing the fractal parser using a file from the data directory.
* This test will fail if this is not done. 
* I asked Jaxton If this technique was acceptable, he said it is ok as long as I make note of it in the README, which I am currently doing. Thanks!


## Background story

Our firm has been contracted to help a mathematician take his amazing
one-million dollar idea to market.  Our client specializes in the field of
complex dynamics, which, frankly, is well above my pay grade, but so is
programming to him.  He has a passion for mathematics education and wants to
take his programs to the K-12 system to teach middle and high-school students
all about the beauty of complex numbers and repeated, tedious calculations.  I
didn't have the heart to tell him that there are already dozens of websites
doing what he wants to do for free; if his inability to use Google keeps us in
steady work, who am I to set him straight?

He has created a few prototype programs intended for high school math students.
He quickly realized that creating user-friendly software is perhaps more
difficult than understanding complex dynamics.  This is where we come in.

Our contract is to adapt his programs into a complete *Programming Systems
Product*.  We must also make it usable by non-programmers, which means that
instead of controlling the program by changing hard-coded data within the
source code it must accept configuration files from the command-line and
adjust its runtime behavior accordingly.

Now, I realize that asking a user to create configuration files and run a
program from the command-line is no longer considered user-friendly in the
21st century.  We have two teams working on this project: one team will be
creating a GUI which is what the students will ultimately interact with.  This
GUI will drive the core program that you will create.  Your responsibility is
to make sure that your piece of the Program System adheres to the
configuration file format that the GUI team has defined, as well as the
command-line interface they are expecting.

It is not strictly necessary for you to understand the math behind these
fractals in order to refactor this program.  To be completely honest with you,
I don't understand them all that well myself.

But don't let your ignorance stop you from fixing up this code.  If you are
patient and work slowly, relying on tests and git, you can carefully change the
code and not make a worse mess out of it.

If you are really dying to know more about these fractals, you'll find the
section at the bottom useful.


## Running the starter code

One program and two modules are provided:

0.  `src/main.py` is the driver and main entry point for the program
1.  `src/mbrot_fractal.py` is responsible for drawing images of the Mandelbrot set
2.  `src/julia_fractal.py` draws images of the Julia set, which uses a slightly modified formula

This program has a simple command line syntax:

```
$ python src/main.py FRACTAL_NAME
```

`FRACTAL_NAME` is the name of a fractal image this program is capable of
producing.  When you run one of the programs without this argument, it will
list names of images it can draw and quits.  The same happens when an
unrecognized `FRACTAL_NAME` is given.

If you use PyCharm you should create **Run configurations** to launch the
program with various arguments.


--------------------------------------------------------------------------------

## What the heck are these fractal things anyway? *OPTIONAL READING*

As stated above, understanding how the fractal programs work isn't strictly
necessary to refactor this code.  You understand enough of the Python language
to make the simple changes that are necessary.

However, some of you won't feel confident until you better understand what's
going on with the fractals.

*   Our program uses the [Escape-Time](https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set) plotting algorithm
*   The points *inside* the cardioid are the Mandelbrot set
    *   The escape-time algorithm gets stuck in an infinite loop for points within the Mandelbrot set
    *   Capping the number of iterations prevents the program from hanging
*   The colorful edges just outside of the Mandelbrot set are where things are interesting


### Interactive Mandelbrot Viewer Demo

To help you better understand the Escape-Time algorithm I have provided an
interactive Mandelbrot program [demo/interactive.py](./demo/interactive.py)

*   Instead of coloring individual pixels, this program colors a block of
    pixels at once.
    *   It's a low-res fractal plotter.
*   Left-Clicking the image will paint a square using the same algorithm that
    the [src/mbrot_fractal.py](./src/mbrot_fractal.py) program uses, except this
    program prints the values of the Z parameter at each iteration to the
    console in addition to showing the iteration count in the image.
*   Right-Clicking the Canvas reveals the entire image.

Reading the demo program's source code, running it in the debugger and reading
its output may help you better understand how your program produces its images.

**Important:** `demo/interactive.py` is provided for your amusement and
benefit.  It is *not* a part of the assignment, and you *are not* required to
improve, test or document it.


### Online resources

*   The difference between the [Mandelbrot and Julia sets](http://usefuljs.net/fractals/docs/julia_mandelbrot.html)
*   [Interactive Browser Fractal Viewer](http://usefuljs.net/fractals/)
*   [XaoS](https://xaos-project.github.io/) - a *smooth* desktop fractal zoomer
*   [Fractint](http://eyecandyarchive.com/Fractint/) - the classic *fast* old-school fractal zoomer
*   YouTube videos that I like:
    *   [D!NG - The Mandelbrot Set](https://youtu.be/MwjsO6aniig?t=70)
    *   [Veritasium - this equation will change how you see the world](https://youtu.be/ovJcsL7vyrk?t=410)
    *   [The Mandelbrot Set - Numberphile](https://www.youtube.com/watch?v=NGMRB4O922I)
