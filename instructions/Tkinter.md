# Tkinter Installation & Troubleshooting

The starter code is runnable out-of-the-box.  If it doesn't work on your computer, check this document for instructions.  If you still have trouble, contact DuckieCorp management with a bug report.

**Include:**

*   A brief description of
    0.  What you did (include the command that you ran)
    1.  What you expected to happen
    2.  What actually happened
*   Copy & paste the full text of error messages printed to the console
*   A screenshot of the Tkinter window, if the problem involves incorrect graphical output

**Do NOT include:**

*   Screenshots of your terminal error messages
*   Screenshots of your IDE
    *   Plain text is much better

This document will be updated as we learn more details.  Do not edit your copy of this file in your repository unless you want to deal with **Git merge conflicts**!


## Windows + Python installed from Python.org

*   Tkinter should already be installed and working
*   If you get this error: `ModuleNotFoundError: No module named 'tkinter'`, you are most likely running a different version of Python than what you expect
    *   When you run the command `which python`, you should **NOT** see `WindowsApps` as part of its path

### Fix

*   Locate where the Python.org installer put `python.exe`
    *   Typically this is found under `C:\Users\USERNAME\AppData\Local\Programs\Python`
    *   Update your system's PATH, open a new Bash terminal, and try again


## Windows + Python installed from Windows App Store

*   Tkinter should already be installed and working
    *   Nevertheless, I don't recommend this version of Python; it barely works
*   You can tell that you're using Python from the Windows App Store when the command `which python` shows `WindowsApps` as part of its path

### Fix

*   Re-install Python from a more reputable source
        *   Update your system's PATH, open a new Bash terminal, and try again


## Linux: Arch-based distributions (Manjaro, Artix, etc.)

While Arch Linux ships Python 3 with the `Tkinter` module, it doesn't automatically provide the Tcl/Tk system it depends on.  When you run the fractal viewer, you'll instead see an error like this:

```
$ python src/main.py
Traceback (most recent call last):
  File "/home/fadein/cs1440-falor-erik-assn4/src/main.py", line 29, in <module>
    import julia_fractal as julia
  File "/home/fadein/cs1440-falor-erik-assn4/src/julia_fractal.py", line 28, in <module>
    import turtle
  File "/usr/lib/python3.9/turtle.py", line 107, in <module>
    import tkinter as TK
  File "/usr/lib/python3.9/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ImportError: libtk8.6.so: cannot open shared object file: No such file or directory
```

### Fix

Install the `tk` package:

```
$ sudo pacman -S tk
```

*(Note: this command may also install other necessary dependencies, such as `Tcl`)*


## Linux: Debian-based distributions (Ubuntu, Mint, etc.)

**TBD**

### Fix

```
$ sudo apt update
$ sudo apt install python3-tk
```

*(Note: this command may also install other necessary dependencies, such as `Tcl`)*
