def solution(A):
    A.sort()
    N = len(A)

    if N == 0:
        return 1  
    if A[-1] == N:
        return (N+1)

    for i in range(1,N+1):
        if i != A[i-1]:
            return i 
    pass
  
  print(solution([2, 3, 1, 5]))
