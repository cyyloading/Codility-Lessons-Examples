
def solution(A):
    min_diff = 10**8  # set a large enough value: (the posible largest value of N)*(the posible largest value of A) = 100,000*1,000 = 10**8
    N = len(A)
    left_sum = 0
    right_sum = sum(A)

    for i in range(1,N):
        left_sum = left_sum + A[i-1]
        right_sum = right_sum - A[i-1]
        abs_diff = abs(left_sum - right_sum)
        if abs_diff < min_diff:
            min_diff = abs_diff
    
    return min_diff
    pass

print(solution([3, 1, 2, 4, 3]))
print(solution([-3, 1, -2, 4, 3]))
