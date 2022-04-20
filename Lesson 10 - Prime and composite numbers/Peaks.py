def solution(A):
    N = len(A)
    if N<3:
        return 0
    
    P = [] # to storage the index of peak
    for i in range(1,N-1):
        if A[i-1]<A[i] and A[i]>A[i+1]:
            P.append(i)
    if len(P)==0:
        return 0
    elif len(P)==1:
        return 1
    

    for i in range(len(P),0,-1):
        if N%i != 0:
            continue
        
        block_len = N//i
        c = [0]*i  # to storage the number of peak located in the ith block
        count = 0  # used to calculate the total number of blocks that contains peak(s) 

        for j in range(len(P)):
            loc_block = P[j]//block_len # loc_block means the peak with index P[j] will locate in 'loc_block', for example if the length of each block is 4, then peak with index 3 will locate in the first (0th) block in c 
            if c[loc_block]==0: # if there is 0 peak in 'loc_block' so far, then the number of peak in this block will increase 1
                c[loc_block]=1
                count += 1
        if count==i:
            return i       
    pass
  
print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
