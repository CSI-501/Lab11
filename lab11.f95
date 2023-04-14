program lab11
    ! Nicholas Maynard
    ! CSI 501
    ! Lab 11
    ! 03/13/2023
    ! This program performs
  
    ! Clear out the memory
  implicit none
  
  ! Declare our Variables
  real :: tFinal, h, y, func
  integer :: n, i

  ! Input user values
  print*,'Enter a value for final time:'
  read*, tFinal

  print*,'Enter a value for step size:'
  read*, h

  print*,'Enter a value for initial y:'
  read*, y

  ! Get our number of iterations.
  n = int(tFinal / h)

  ! Open output file
  open(13, file='output.txt')

  ! Write the initial values
  write(13, *) 0, y

  ! Perform our Eulers method.
  do i=1, n
    y = y + h * func((i*h), y)
    write(13, *) (i * h), y
  enddo
  
end program lab11

function func(t, y) result(res)
  ! Clear memory
  implicit none

  ! Declare our variables
  real :: t, y, res

  ! Compute Function
  res = 1 - (2 * y**2) + (5 * t) - t**2
end function func