'''
CopyRight 2022
@author Yuyang Chen
All rights reserved. 
'''


def solution(N):
    A = bin(N)[2:]
    max_count = 0
    loc_count = 0
    check =  False
    for i in range(len(A)):
        if A[i]==str(1):
            check = True
            max_count = max(max_count,loc_count)
            loc_count = 0
        else:
           if check:
                loc_count += 1
    return max_count
    pass
  
 
'''
 # Second answer:

def solution(N):
    A = bin(N)[2:]
    max_count = 0
    loc_count = 0
    while A[0] != str(1):
      A = A[1:] # delete all '0' before the first '1'
      
    for i in range(len(A)):
        if A[i]==str(1):
            max_count = max(max_count,loc_count)
            loc_count = 0
        else:
            loc_count += 1
    return max_count
    pass
'''

print(solution(1041))
