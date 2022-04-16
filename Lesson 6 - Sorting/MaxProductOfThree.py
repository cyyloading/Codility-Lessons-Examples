def solution(A):
    A.sort()
    # After sorting, the maximum product may happen in 2 situations: 
    # first: the most 2 smallest negative values and 1 maximum positive value
    # second: the most 3 positive largest values
    result = max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])
    return result
    pass
  
print(solution([-3,1,2,-2,5,6]))
