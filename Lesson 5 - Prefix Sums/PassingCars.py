def solution(A):
    N = len(A)
    count_zero = 0 # calculate the number of 0 before element i
    result = 0
    for i in range(N):
        if A[i]==0:
            result += N-i-1 # if A[i] is 0, assume all values after i are 1, then the number of passing increases (N-i-1)
            result -= count_zero # the above 'assumption' results in adding extra 1 into result for each 0 happened before element i
            count_zero += 1  # update the number of 0 before element i
    if result > 1000000000:
        return -1
    else:
        return result
    pass
  
print(solution([0,1,0,1,1]))
