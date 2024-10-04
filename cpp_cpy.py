"""
Python module for import that provides ease-of-use wrapper functions to the C++
functions in cpp_pi.cpp. The cpp file must be compiled as a shared object file. 
Using the C-types and C-interface in c++ allows Python to import and
use these subroutines directly.
"""
import ctypes as ct

def config_cpp():
    """ for setting the configurations in one spot"""
    # c data types, must correspond with C++ code
    inttype = ct.c_int
    floattype = ct.c_double
    # location of the object file
    clib = ct.CDLL('./cpp_pi.so')
    return inttype, floattype, clib


def c_pi(n):
    """ Wrapper for cpp_pi.cpp forcpi circumventing
    :param n: the number of points to examine
    :type n: int
    :return: an estimation of pi
    :rtype: float
    """
    # get the set datatypes and shared library
    inttype, floattype, clib = config_cpp()
    
    # set the function needed from the library
    cpic = clib.forcpi

    # set input datatypes
    cpic.argtypes = [inttype,]
    # set output datatypes
    cpic.restype = floattype
    # call the function
    pi = cpic(inttype(int(n)))
    return pi


if __name__ == '__main__':

    print(c_pi(1000))