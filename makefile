# Disable all of make's built-in rules (similar to Fortran's implicit none)
MAKEFLAGS += --no-builtin-rules --no-builtin-variables
FC1 := gfortran
FC2 := f2py

CC1 := g++

RM := rm -f

CFLAGS1 = -shared -O3
CFLAGS2 = --opt='-O3' -c

CCFLAGS1 = -shared -O3 -c -fPIC cpp_pi.cpp -o cpp_pi.o
CCFLAGS2 = -shared -Wl,-soname,cpp_pi.so -o cpp_pi.so cpp_pi.o

all: 
#	gfortran -shared -O3 -o fpi_c.so fpi.f90
	$(FC1) $(CFLAGS1) -o fpi_c.so fpi.f90
#	f2py --opt='-O3' -c fpi.f90 -m fpi	
	$(FC2) $(CFLAGS2) fpi.f90 -m fpi

	$(CC1) $(CCFLAGS1)
	$(CC1) $(CCFLAGS2)