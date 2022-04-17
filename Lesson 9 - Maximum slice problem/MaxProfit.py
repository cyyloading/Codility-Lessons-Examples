def solution(A):
    N = len(A)
    if N==0:
        return 0

    min_a = A[0]
    max_a = A[0]
    profit = 0
    for i in range(1,N):
        if min_a > A[i]:
            min_a = A[i]
            max_a = A[i]  # Update the max_a in case of extreme situation such as:[6,5,4,3,2,1] (descending)
        if max_a < A[i]:
            max_a = A[i]
        if profit < max_a - min_a:
            profit  = max_a - min_a
    return profit
    pass

print(solution([23171,21011,21123,21366,21013,21367]))
print(solution([5,2,3,4,1]))
print(solution([5,2,3,4,1,5]))
