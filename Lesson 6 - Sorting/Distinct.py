def solution(A):
    A = set(A)
    return len(A)
    pass


  '''
# Or
def solution(A):
    count = [0]*2000001
    N = len(A)
    for i in range(N):
        count[A[i]] += 1
    
    num = 0
    for i in count:
        if i > 0:
            num += 1
    return num
    pass

# Or
def solution(A):
    N = len(A)
    B = {}
    for i in range(N):
        if A[i] not in B:
            B[A[i]] = 1    
    return len(B)
    pass
'''
  
print(solution([2,1,1,2,3,1]))
