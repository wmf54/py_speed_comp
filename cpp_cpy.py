import ctypes as ct
import numpy as np

def config_cpp():
    """ for setting the configurations in one spot"""
    # c data types, must correspond with fortran code
    inttype = ct.c_int
    floattype = ct.c_double
    # location of the object file
    clib = ct.CDLL('./cpp_pi.so')
    return inttype, floattype, clib


def c_pi(n):
    inttype, floattype, clib = config_cpp()
    
    cpic = clib.forcpi

    cpic.argtypes = [inttype,]
    cpic.restype = floattype
    #pi = cpic(inttype(n))
    pi = cpic(inttype(int(n)))
    return float(pi)


if __name__ == '__main__':

    print(c_pi(1000))