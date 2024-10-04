// g++ -shared -c -fPIC shared_module.cpp -o square.o
// g++ -shared -Wl,-soname,cpplib.so -o cpplib.so square.o
#include <random>

extern "C" 
double forcpi(int n)
{
    double cpi=0.0, x=0.0, y=0.0, r=0.0;
    int n_circle=0;
    std::default_random_engine generator;
    std::uniform_real_distribution<double> distribution(0.0, 1.0);

    for (int i=0; i<n; i++) {
        x = distribution(generator);
        y = distribution(generator);

        r = x*x + y*y;
        
        if (r<=1.0) {
            n_circle += 1;
        }

    }

    cpi = 4.0 * ((1.0*n_circle) / (1.0*n));
    //std::cout << cpi;
    return cpi;
}