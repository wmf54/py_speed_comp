# Comparison of speed in Python over an increasing number of iterations using different strategies

## Methodology
Using Monte Carlo simulations to estimate pi is a common metric for testing the speed and efficiency of code and 
machines. The algorithm and subsequent code is simple, and it is easily vectorized. Pi is estimated by generating
random points between 0 and 1 in the x and y coordinates then taking the ratio of the number of points that lie in a 
circle and the number of points that lie in a square. Generate numbers randomly between 0 and 1. Calculate the radius 
and if the radius is less than 1, it lies in the circle. All points generated lie in the square by default. The metric 
of comparison used was the 5-time average execution time over each number of iterations to estimate pi.


## Different strategies evaluated
- Pure Python
- Vectorized Python with NumPy
- Pure Python with Numba JIT
- Vectorized Python with Numba JIT
- Fortran compiled for Python with f2py
- Vectorized Fortran compiled for Pyton with f2py
- Fortran compiled into a .so file using the iso_c_binding module
- Vectorized Fortran compiled into a .so file using the iso_c_binding module

## The results are in the figure below.
![Alt text of the image](https://github.com/wmf54/py_speed_comp/blob/main/Timing_Image_V2.png)


#### Differences in the Fortran implementations
Both Fortran implementations come from the same source code file, and the same
Fortran module and the same two subroutines. The difference is in the way they are
compiled into a Python importable module file. A common way for interfacing libraries
coded in other languages with Python is to use tools that automatically generate modules or
wrapper functions, like SWIG. f2py is a tool packaged with numpy that automatically
generates interfaces between Fortran and Python. However, modern Fortran also facilitates
interfacing with C more directly throught the iso_c_binding module. Python interfaces with C
modules natively through the built-in ctypes module. Both of these latter two options are explored.
The benefits of f2py come in the relative ease-of-use (the automation of it). While the Fortran C
interface benefits from directo support through the Fortran language developers and Python
developers via the both's goal for an ease of interfacing with C modules. However, more explicit
care with typing is required through this path. The file `fpi_cpy.py` handles the Python side
for dealing with the explicit C-typing.


## Compiling the Fortran source code
The code was compiled using Windows Subsystem for Linux (WSL).
A makefile is provided that was used to build the modules used.
Here are versions used:
Ubuntu 22.04.2 LTS
gfortran 11.4.0
Python 3.10.12
numpy 1.24.4

#### Use make to build the library files
