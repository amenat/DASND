def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print('ValueError: Math domain error. number must be in range [0, infty)')
    lo = 0
    hi = number

    while hi >= lo:
        mid = (lo + hi) // 2
        if mid * mid <= number and (mid+1) * (mid+1) > number:
            return mid
        elif mid * mid > number:
            hi = mid - 1
        else:
            lo = mid + 1



print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# one test case to rule them all
print('pass' if all(sqrt(x) == int(x**0.5) for x in range(100000)) else 'Fail')

print('Check negative values: sqrt(-5)')
print ("Pass" if  (5 == sqrt(-5)) else "Fail")

