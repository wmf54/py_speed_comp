module fpi
    implicit none
    contains

        ! Subroutine one uses a do-loop
        subroutine dofpi(n, cpi)
            intent(in) n
            intent(out) cpi
            integer :: n, i
            double precision :: x, y, r
            double precision :: n_circle, n_square, cpi
            
            ! initialize the number of points in the circle and the number in the square to zero
            n_circle = 0.0
            n_square = 0.0
            
            ! loop over the number of iterations
            do i = 1, n
                ! generate random value for x and y on [0.0, 1.0)
                call random_number(x)
                call random_number(y)

                ! calculate the radius
                r = x * x + y * y

                ! any less than or equal to 1 are in the circle
                if (r .le.  1) then
                    n_circle = n_circle + 1

                end if

                ! all fall in the square
                n_square = n_square + 1

            end do

            ! estimate pi
            cpi = (4 * (n_circle / n_square))
        end subroutine

        ! Subroutine two uses vectorized array broadcasting
        subroutine vfpi(n, cpi)
            intent(in) n
            intent(out) cpi
            integer :: n
            double precision, dimension(n) :: x, y, r
            double precision :: n_circle, n_square, cpi
            
            ! initialize the number of points in the circle and the number in the square to zero
            n_circle = 0.0
            n_square = 0.0
            
            ! generate random value for x and y on [0.0, 1.0) over the entire array x and y
            call random_number(x)
            call random_number(y)

            ! calculate the radius
            r = x * x + y * y

            ! any less than or equal to one are in the circle
            n_circle = count(r<=1)

            ! all fall in the square
            n_square = n

            ! estimate pi            
            cpi = (4 * (n_circle / n_square))

        end subroutine




end module 
