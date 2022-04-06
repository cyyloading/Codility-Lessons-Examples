def solution(A):
    B = {}  # create a empty dict to storage the distinct values in A and their corresponding frequency
    for i in A:
        if i not in B:
            B[i] = 1
        else:
            B[i] += 1
    
    for i in B: 
        if B[i]%2 != 0:  # check if the frequency of the value is not even times
            return i
    pass
  
print(solution([9,3,9,3,9,7,9]))
print(solution([9,3,9,3,9,7,7]))
