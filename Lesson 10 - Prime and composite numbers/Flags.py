#Better explaination is provided by CodeTrading: https://www.youtube.com/watch?v=6KK2eglhvdQ
def solution(A):
    N = len(A)
    if N<3:
        return 0

    peak = []
    for i in range(1,N-1):
        if A[i-1]<A[i] and A[i]>A[i+1]:
            peak.append(i)
    
    if len(peak)==0:
        return 0
    if len(peak)==1:
        return 1

    max_flag = 1
    for i in range(min(len(peak),int(N**0.5)+1),0,-1):
        count = 1
        start = 0
        for j in range(1,len(peak)):
            if (peak[j]-peak[start]) >= i and count<i:
                count += 1
                start = j
                
        if count<max_flag:
            return max_flag  # if the maximum posible plag number is lower than current max_flag, no need to continue to check the smaller posible 'count' value
        else:
            max_flag = count
            
    return max_flag        
    pass
  
print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
print(solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1]))
