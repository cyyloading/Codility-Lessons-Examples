def solution(A):
    A = set(A) # if without set(A), the time cimplexity will become O(N**2)

    for i in range(1, 1000001):
        if i not in A:
            return i
    pass

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([-1, -3]))
