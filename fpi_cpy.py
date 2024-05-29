"""
Python module for import that provides ease-of-use wrapper functions to the Fortran
subroutinesi n fpi.f90. The Fortran file must be compiled as a shared object file. 
Using the C-types and explicit C-interface in Fortran allows Python to import and
use these subroutines directly without the need for f2py or another tool.
"""
import ctypes as ct


def config():
    """ for setting the configurations in one spot"""
    # c data types, must correspond with fortran code
    inttype = ct.c_int64
    floattype = ct.c_double
    # location of the object file
    flib = ct.CDLL('./fpi_c.so')
    return inttype, floattype, flib

def fpi(n):
    """ Wrapper for fpi.f90 circumventing f2py
    :param n: the number of points to examine
    :type n: int
    :return: an estimation of pi
    :rtype: float
    """
    inttype, floattype, flib = config()

    # the desired subroutine to use
    fpic = flib.dofpi

    # initializing pi since this uses a subroutine
    cpi= floattype(0.0)

    # explicitly define the expected types 
    fpic.argtypes = (ct.POINTER(inttype), ct.POINTER(floattype))

    # execute the subroutine
    fpic(inttype(n), cpi)
    
    # return the value of a pi as a python float
    return cpi.value

def vfpi(n):
    """ Wrapper for fpi.f90 circumventing f2py
    :param n: the number of points to examine
    :type n: int
    :return: an estimation of pi
    :rtype: float
    """
    inttype, floattype, flib = config()

    # the desired subroutine to use
    fpic = flib.vfpi

    # initializing pi since this uses a subroutine    
    cpi= floattype(0.0)

    # explicitly define the expected types     
    fpic.argtypes = (ct.POINTER(inttype), ct.POINTER(floattype))

    # execute the subroutine
    fpic(inttype(n), cpi)
    
    # return the value of a pi as a python float
    return cpi.value



if __name__ == '__main__':

    n = 10000

    print(fpi(n), vfpi(n))
