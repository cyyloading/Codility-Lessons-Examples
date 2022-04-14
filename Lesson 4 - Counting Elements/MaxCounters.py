# The score of this code is 88%, it's the simplest method with highest score I can think out currently. 
# will update if have new better idea.
# Time complexity: O(N+M)

def solution(N, A):
    counter = [0]*N
    M = len(A)
    max_val = 0 # define max_val as global variable, for extreme situation such as: (1,[2,1,1,2,1]), operates 'max counter' at the first momnent A[0]

    for i in range(M):
        if A[i]>=1 and A[i]<=N:
            counter[A[i]-1] += 1
            if max_val<counter[A[i]-1]:
                max_val = counter[A[i]-1]
        else:
            counter = [max_val]*N
    return counter
    pass
    
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
    print(solution(1,[2,1,1,2,1]))
