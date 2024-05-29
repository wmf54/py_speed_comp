module fpi
    use, intrinsic :: iso_c_binding, only: rk => c_double, ik => c_int32_t
    implicit none
    contains

        ! Subroutine one uses a do-loop
        subroutine dofpi(n, cpi) bind(C, name='dofpi')
            integer(ik), intent(in) :: n
            real(rk), intent(out) :: cpi
            integer(ik) :: i
            real(rk) :: x, y, r
            real(rk) :: n_circle, n_square
            
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
                if (r<=1) then
                    n_circle = n_circle + 1

                endif

                ! all fall in the square
                n_square = n_square + 1
                
            enddo

            ! estimate pi
            cpi = (4 * (n_circle / n_square))
            
        end subroutine

        ! Subroutine two uses vectorized array broadcasting
        subroutine vfpi(n, cpi) bind(C, name='vfpi')
            integer(ik), intent(in) :: n
            real(rk), intent(out) :: cpi
            real(rk), dimension(n) :: x, y, r
            real(rk) :: n_circle, n_square
            
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
