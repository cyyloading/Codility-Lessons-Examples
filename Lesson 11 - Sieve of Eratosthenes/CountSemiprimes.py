# Time complexity: O(N * log(log(N)) + M)

def solution(N, P, Q):
    result = []
    if N<4:
        return [0]
    
    # find out all primes that is less than N
    prime = [1]*(N+1)
    prime[0]=prime[1]=0
    i = 2
    for i in range(2,int(N**0.5)+1):
        if prime[i]==1:
            k=i*i
            while k<=N:
                prime[k]=0
                k += i   

    # get all semiprimes that is less than N
    semiprime = [0]*(N+1)
    for i in range(N+1):
        for j in range(N+1):
            if prime[i]==1 and prime[j]==1 and i*j<=N:
                semiprime[i*j]=1
            if i*j>N:
                break


    # storage the total number of semiprime by index<=i into count[i], similar use dynamic program to calculate the accumulated number of semiprimes
    count = [0]*(N+1)
    for i in range(1,N+1):
        if semiprime[i]==1:
            count[i] = count[i-1]+1
        else:
            count[i] = count[i-1]


    for i in range(len(P)):
        result.append(count[Q[i]]-count[P[i]-1])
    
    return result        
    pass

solution(26,[1,4,16],[26,10,20])
