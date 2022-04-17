def solution(A):
    N = len(A)
    loc_max = A[0]
    max_sum = A[0]

    for i in range(1,N):
        if (loc_max + A[i]) > A[i]:
            loc_max =  loc_max + A[i]
        else: 
            loc_max = A[i]
        
        if max_sum < loc_max:
            max_sum = loc_max
    return max_sum
    pass

print(solution([3,2,-6,4,0]))
