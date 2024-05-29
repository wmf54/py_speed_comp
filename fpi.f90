! Fortran module with two subroutines for estimating pi using Monte-Carlo method. Intended for 
! compilation as a module to import and use in Python. Uses C-types and bind() to allow for 
! direct import and use in Python with Python built-in ctypes module.
module fpi
    use, intrinsic :: iso_c_binding, only: rk => c_double, ik => c_int64_t
    implicit none
    contains

        ! Subroutine  for estimating pi using a single do-loop
        subroutine dofpi(n, cpi) bind(C, name='dofpi')
            integer(ik), intent(in) :: n
            real(rk), intent(out) :: cpi
            integer(ik) :: i
            real(rk) :: x, y, r 
            real(rk) :: n_circle, n_square
            
            ! initialize the number of points in the circle and the number in the square to zero
            n_circle = 0_rk
            n_square = 0_rk
            
            ! loop over the number of iterations
            do i=1, n
                ! generate random value for x and y on [0.0, 1.0)
                call random_number(x)
                call random_number(y)

                ! calculate the radius
                r = x*x + y*y

                ! any less than or equal to 1 are in the circle
                if (r<=1_rk) then
                    n_circle = n_circle + 1_rk
                end if

                ! all fall in the square
                n_square = n
                
            end do

            ! estimate pi
            cpi = 4_rk * (n_circle / n_square)
            
        end subroutine

        ! Subroutine  for estimating pi using vectorized array broadcasting
        subroutine vfpi(n, cpi) bind(C, name='vfpi')
            integer(ik), intent(in) :: n
            real(rk), intent(out) :: cpi
            real(rk), dimension(n) :: x, y, r
            real(rk) :: n_circle, n_square
            
            ! initialize the number of points in the circle and the number in the square to zero
            n_circle = 0_rk
            n_square = 0_rk
            
            ! generate random value for x and y on [0.0, 1.0) over the entire array x and y
            call random_number(x)
            call random_number(y)

            ! calculate the radius
            r = x*x + y*y

            ! any less than or equal to one are in the circle
            n_circle = count(r<=1_rk)

            ! all fall in the square
            n_square = n

            ! estimate pi            
            cpi = 4_rk * (n_circle / n_square)

        end subroutine

end module 
