'''
CopyRight 2022
@author Yuyang Chen
All rights reserved. 
'''


def solution(A, K):
    N = len(A)
    if N == 0: #check if A is empty
        return []

    a = K%N  # calculate the remainder of K divided by N
    if a == 0: # check if the remainder is 0, if Yes, return the original A
        return A
    else:
        result = A[N-a:] + A[:N-a] # Can directly return result without check if a==0; Just for better understand
        return result
    pass


print(solution([1, 2, 3, 4], 4))
print(solution([3, 8, 9, 7, 6], 13))
