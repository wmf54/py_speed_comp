/*
C++ functions for estimating pi using Monte-Carlo method. Intended for 
compilation as a module to import and use in Python. Uses extern "C" to allow for 
direct import and use in Python with Python built-in ctypes module.
*/
#include <random>

extern "C" 
double forcpi(int n)
{
    double cpi=0.0, x=0.0, y=0.0, r=0.0;
    int n_circle=0;
    
    // Setup the random generator
    std::default_random_engine generator;
    // Set the uniform distribution
    std::uniform_real_distribution<double> distribution(0.0, 1.0);

    // Loop over the number of points
    for (int i=0; i<n; i++) {

        // grab a random x,y position
        x = distribution(generator);
        y = distribution(generator);

        // Determine the radius
        r = x*x + y*y;
        
        // add to the circle count if it lands in the circle
        if (r<=1.0) {
            n_circle += 1;
        }

    }

    // Estimate pi as 4 x the ratio of points in the circle and square
    cpi = 4.0 * ((1.0*n_circle) / (1.0*n));
    return cpi;
}