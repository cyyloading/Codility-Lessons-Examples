def solution(A):
    N = len(A)
    if N==0:
        return -1
    dominator = -1
    B = A.copy()
    A.sort()
    candidate = A[N//2]
    count = 0
    for i in range(N):
        if A[i]==candidate:
            count += 1
    if count>N//2:
        dominator = candidate
        return B.index(dominator) # Because original A has been sorted, then original index is changed. B is a copy of A
    return -1
    pass

print(solution([3,4,3,2,3,-1,3,3]))
