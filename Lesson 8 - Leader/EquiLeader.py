def solution(A):
    # Idea: if element i is leader of A, A is divided into 2 sequences. If sequence has leader, the leader still is element i
    # 1. Calculate the leader of A if there is leader
    # 2. use 'enumerate' to find out the leader's index in the original A and the total number of leader before current index (inclusive)
    # 3. storage the index and the total number of leader to dict (key is index, value is the number of leader so far)
    # 4. if the element j is not leader, its value (total number of leader) in dict will be same with the maximum number of leader so far
    # 5. loop the dict, key is the index of A, corresponding value is the total number of leader until this index
    # for each i in dict, the left side of i is the first sequence, right side of i is the second sequence
    # just make sure if the number of i in left sequence is larger than the half of left sequence and the number of i in right is larger than the half of right sequence, then equileader increase 1 
    
    N = len(A)
    B = A.copy()
    A.sort()
    leader = -1
    candidate = A[N//2]
    count1 = 0

    for i in range(N):
        if A[i]==candidate:
            count1 += 1
    if count1>N//2:
        leader = candidate
    
    prefix_sum = {}
    count2 = 0
    for pos,val in enumerate(B):
        if val==leader:
            count2 += 1
            prefix_sum[pos]=count2
        else:
            prefix_sum[pos]=count2

    count3 = 0
    for i in prefix_sum.keys():
        a = prefix_sum.get(i)
        if a>(i+1)//2 and (count1-a)>(N-i-1)//2: # a is the number of leader in left sequence, then the number of leader in right sequence will be equal to total number of leader count1 in A minus a: (count1-a)
            count3 += 1                     # the left sequence contains (i+1) integers, then right sequence contains (N-i-1) integers
    return count3

print(solution([4, 3, 4, 4, 4, 2]))
print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
