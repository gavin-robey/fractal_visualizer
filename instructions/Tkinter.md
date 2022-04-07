# Tkinter Installation & Troubleshooting

## Table of Contents

*   [Windows + Python installed from Python.org](#windows-python-installed-from-pythonorg)
*   [Windows + Python installed from Windows App Store](#windows-python-installed-from-windows-app-store)
*   [Linux: Arch-based distributions (Manjaro, Artix, etc.)](#linux-arch-based-distributions-manjaro-artix-etc)
*   [Linux: Debian-based distributions (Ubuntu, Kubuntu, Xubuntu, Mint, etc.)](#linux-debian-based-distributions-ubuntu-kubuntu-xubuntu-mint-etc)
*   [macOS Monterey](#macos-monterey)


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
$ sudo pacman -Sy
$ sudo pacman -S tk
```

*(Note: this command may also install other necessary dependencies, such as `Tcl`)*


## Linux: Debian-based distributions (Ubuntu, Kubuntu, Xubuntu, Mint, etc.)

On these systems you may see an error similar to this:

```
$ python3 src/main.py
Traceback (most recent call last):
  File "/home/ubuntu/cs1440-falor-erik-assn4/src/main.py", line 5, in <module>
    import julia_fractal as julia
  File "/home/ubuntu/cs1440-falor-erik-assn4/src/julia_fractal.py", line 4, in <module>
    import turtle
  File "/usr/lib/python3.9/turtle.py", line 107, in <module>
    import tkinter as TK
ModuleNotFoundError: No module named 'tkinter'
```

### Fix

```
$ sudo apt update
$ sudo apt install python3-tk
```

*(Note: this command may also install other necessary dependencies, such as `Tcl`)*


## macOS Monterey

*From Python.org: If you are using macOS 12 Monterey or later, you may see problems with tkinter-based applications. The most recent versions of python.org installers (for 3.10.0 and 3.9.8) have patched versions of Tk to avoid these problems. They should be fixed in an upcoming Tk 8.6.12 release.*

This means that Tkinter applications won't properly work with the Python 3 bundled with macOS 10.6 - 12.2.  The most common symptom is that the Tkinter window is black and appears unresponsive while the program runs.

### Fix

The remedy is to download and install the latest Python 3 package directly from python.org.

0.  Browse to the [python.org downloads page](https://www.python.org/downloads/)
1.  Download the latest build of Python 3 for macOS
2.  Launch the .pkg installer program
3.  Click through the installer
4.  When the installer finishes, a Finder window is opened that contains a few more programs to run.
    *   Run `Install Certificates.command`
    *   Run `Update Shell Profile.command`
5.  Open a new Terminal and run `python3 --version` to make sure the reported version number matches what you just installed
