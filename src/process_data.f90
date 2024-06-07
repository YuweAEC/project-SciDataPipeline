! process_data.f90
program process_data
    implicit none
    integer, parameter :: n = 10
    real :: data(n)
    real :: mean
    integer :: i

    ! Initialize data array
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]

    ! Calculate the mean
    mean = sum(data) / n

    ! Print the result
    print *, 'Mean of the array:', mean
end program process_data
