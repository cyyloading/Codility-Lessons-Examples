def solution(A):
    N = len(A)
    if N<3:
        return 0
    
    A.sort()
    for i in range(N-2):
        sum_two = A[i] + A[i+1]
        if sum_two > A[i+2]:
            return 1
    return 0
    pass

print(solution([10,2,5,1,8,20]))
print(solution([10,50,5,1]))
