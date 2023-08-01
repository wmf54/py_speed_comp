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

## The results are in the figure below.
![Alt text of the image](https://github.com/wmf54/py_speed_comp/blob/main/Timing_Image_V2.png)


## Compiling the Fortran source code (your mileage may vary)
I compiled the Fortran code on a Cray machine running SUSE Linux Enterprise Server 15 SP3.

#### Here is my process of events.
initialize conda through loading a bash script with the stuff from conda init

`source ~/Bash_Scripts/init_conda`

activate my conda environment with 

`conda activate ~/venvs/exo_env`

swap programming environment to gain access to gnu compiler
`module swap PrgEnv-cray/6.0.10 PrgEnv-gnu` 

compile the source code for Python using gnu compiler. f2py should be able to find the compiler itself if everythin is done right

`f2py -c fpi.f90 -m fpi`

Check that it is importable and functioning. 

`python -c "from fpi import fpi; print(fpi.dofpi(1000)), print(fpi.vfpi(1000))"`
