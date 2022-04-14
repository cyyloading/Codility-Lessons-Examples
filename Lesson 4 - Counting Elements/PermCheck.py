def solution(A):
    A.sort()
    B = set(A)
    if len(B)==len(A) and A[-1]==len(A):  # check if A contains all elements from 1 to N, and only once. Also check if the maximum value in A after sorting is equal to N
        return 1
    else:
        return 0
    pass

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))
print(solution([1, 1, 3]))
