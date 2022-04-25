# Time complexity: O(N * log(N))
def solution(A):
    N = len(A)
    max_A = max(A)
    count = [0]*(max_A + 1)  # used to count the number of each element in A
    for i in A:
        count[i] += 1


    result = []
    B = set(A)  # only count the number of divisor for distinct elements
    temp = {} 
    for i in B:
        num_div = 0
        j = 1
        while j*j<i:
            if i%j==0:
                num_div += (count[j]+count[i//j]) # don't forget to count the number of the divisor that is larger than j
            j += 1
        if j*j==i:
            num_div += count[j]
        non_div = N - num_div
        temp[i] = non_div
    
    for i in A:
        result.append(temp[i])

    return result
    pass

print(solution([3,1,2,3,6]))
print(solution([32]))
