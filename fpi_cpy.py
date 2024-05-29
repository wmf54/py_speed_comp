"""
Python module for import that provides ease-of-use wrapper functions to the Fortran
subroutinesi n fpi.f90. The Fortran file must be compiled as a shared object file. 
Using the C-types and explicit C-interface in Fortran allows Python to import and
use these subroutines directly without the need for f2py or another tool.
"""
import ctypes as ct


def fpi(n):
    """ Wrapper for fpi.f90 circumventing f2py
    :param n: the number of points to examine
    :type n: int
    :return: an estimation of pi
    :rtype: float
    """
    # location of the object file
    flib = ct.CDLL('./fpi_c.so')

    # the desired subroutine to use
    fpic = flib.dofpi

    # initializing pi since this uses a subroutine
    cpi= ct.c_double(0.0)

    # explicitly define the expected types 
    fpic.argtypes = (ct.POINTER(ct.c_int32), ct.POINTER(ct.c_double))

    # execute the subroutine
    fpic(ct.c_int32(n), cpi)
    
    # return the value of a pi as a python float
    return cpi.value

def vfpi(n):
    """ Wrapper for fpi.f90 circumventing f2py
    :param n: the number of points to examine
    :type n: int
    :return: an estimation of pi
    :rtype: float
    """

    # location of the object file    
    flib = ct.CDLL('./fpi_c.so')

    # the desired subroutine to use
    fpic = flib.vfpi

    # initializing pi since this uses a subroutine    
    cpi= ct.c_double(0.0)

    # explicitly define the expected types     
    fpic.argtypes = (ct.POINTER(ct.c_int32), ct.POINTER(ct.c_double))

    # execute the subroutine
    fpic(ct.c_int32(n), cpi)
    
    # return the value of a pi as a python float
    return cpi.value



if __name__ == '__main__':

    n = 10000

    print(fpi(n), vfpi(n))
