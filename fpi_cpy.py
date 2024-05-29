import ctypes as ct


def fpi(n):
    """ Wrapper for fpi.f90 circumventing f2py"""
    
    flib = ct.CDLL('./fpi_c.so')

    fpic = flib.dofpi
    cpi= ct.c_double(0.0)
    fpic.argtypes = (ct.POINTER(ct.c_int32), ct.POINTER(ct.c_double))
    fpic(ct.c_int32(n), cpi)
    
    return cpi.value

def vfpi(n):
    """ Wrapper for fpi.f90 circumventing f2py"""
    
    flib = ct.CDLL('./fpi_c.so')

    fpic = flib.vfpi
    cpi= ct.c_double(0.0)
    fpic.argtypes = (ct.POINTER(ct.c_int32), ct.POINTER(ct.c_double))
    fpic(ct.c_int32(n), cpi)
    
    return cpi.value



if __name__ == '__main__':

    n = 10000

    print(fpi(n), vfpi(n))
