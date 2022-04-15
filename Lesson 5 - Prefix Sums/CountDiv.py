def solution(A, B, K):
    # check if A is the multiple of K
    if A%K == 0:
        result = 1
    else:
        result = 0
    
    i = ((A//K)+1)*K # get the first value between A and B that is the multiple of K
    if i > B:
        return result
    else:
        return result + ((B-i)//K + 1) 
    pass

print(solution(6,11,2))
