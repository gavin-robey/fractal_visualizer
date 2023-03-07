# Fractal Visualizer Information and Build instructions

## Project Information
This program uses python and the tk interface module to draw fractals to the screen using both the mandelbrot and julia sets. All example images are stored in the *fractalGallery* directory. Fractal images are created using a file with preset settings. The color palette can be altered from the command line. New fractal settings can be added by creating a configuration file and adding this file to the *data* directory. Instructions on how to do this are stored in both the README in *data* and below in the *Build Instructions*

## Build Instructions

**To run this program use this command:**
```commandline
python src/main.py
```
**This command creates a default fractal image**
* You will be greeted with the following prompts
```commandline
creating default fractal
creating a default palette
Done in 8.507 seconds!
Wrote image default.png
Close the image window to exit the program
```
* You will also have a separate window displaying the default fractal image

*Once you're done with the image, close the window and the program will exit*

![default.png](default.png)


**To create a different type of fractal simply enter the file name of a fractal configuration file**



*Below are all fractal configuration files:*
```commandline
8points.frac	            burningship.frac		    lakes.frac	        spiral-jetty.frac			
fulljulia.frac		    mandelthree.frac		    tip1.frac		unconnected.frac
connected.frac		    leaf.frac		            spiral0.frac	wholly-squid.frac
branches100.frac	    hourglass.frac	            minibrot.frac       tip2.frac		
coral.frac		    mandelbrot-zoomed.frac	    spiral1.frac        tip3.frac
branches256.frac	    invalid.frac	            rabbit-hole.frac    tip4.frac
elephants.frac		    mandelbrot.frac		    starfish.frac		
branches512.frac	    lace-curtians.frac	            seahorse.frac				
enhance.frac	            mandelfour.frac		    tip0.frac		
```

**Chose a fractal configuration then enter the following command:**

*This is a demonstration creating a spiral0.frac fractal*

```commandline
python3 src/main.py data/spiral0.frac
```

*The following prompts will appear as the fractal image is being generated*

```commandline
creating a spiral0 fractal
creating a default palette
Done in 11.098 seconds!
Wrote image spiral0.png
Close the image window to exit the program
```


![spiral0.png](spiral0.png)


**To create a fractal with a new color palette, use these commands:**

```commandline
python3 src/main.py data/spiral0.frac gold
```

or 


```commandline
python3 src/main.py data/spiral0.frac rainbow
```


**Palette commands must be given after the desired fractal, and cannot be given on their own**


*For example this command is illegal:*


```commandline
python3 src/main.py rainbow
```


*How do the configuration files work?*


**In order to create a new configuration file, it must contain all of these items:**

*Mandelbrot must follow these conditions*
```commandline
type: Mandelbrot
pixels: 1024
centerX: -0.693792639088625
centerY: -0.36850658033037173
axisLength: 0.005
pixels: 640
iterations: 512
```


**Mandelbrot types must have the following components:**  *'type', 'centerx' and 'centery', 'axisLength', 'pixels', and 'iterations'* **All seperated by a colon**

*Julia must follow these conditions*
```commandline
type: julia
creal: -1
cimag: 0
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
```

**Julia types must have the following components:**  *'type', 'centerx' and 'centery', 'axisLength', 'pixels', 'iterations' 'creal', and 'cimag'* **All seperated by a colon**

*Components must have the same types and formatting as seen above*



