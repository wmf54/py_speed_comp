# Disable all of make's built-in rules (similar to Fortran's implicit none)
MAKEFLAGS += --no-builtin-rules --no-builtin-variables
FC1 := gfortran
FC2 := f2py

RM := rm -f

CFLAGS1 = -shared -O3
CFLAGS2 = --opt='-O3' -c


all: 
#	gfortran -shared -O3 -o fpi_c.so fpi.f90
#	f2py --opt='-O3' -c fpi.f90 -m fpi
	$(FC1) $(CFLAGS1) -o fpi_c.so fpi.f90
	$(FC2) $(CFLAGS2) fpi.f90 -m fpi
#$(prog):

# create fpi_c.so
#fpi_c.so: fpi.f90
#	gfortran -shared -O3 -o $@^ fpi.f90


#f2py --opt='-O3' -c fpi.f90 -m fpi