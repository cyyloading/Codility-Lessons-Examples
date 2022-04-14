def solution(X, A):
    B = set()  # creat a set to storage distinct elements 
    for pos,val in enumerate(A):
        B.add(val) # add element into set B
        if len(B)==X: # check if B contains all values between 1 to X when the current index is pos
            return pos
    return -1
    pass

print(solution(5,[1, 3, 1, 4, 2, 3, 5, 4]))
