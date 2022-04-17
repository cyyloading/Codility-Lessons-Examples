def solution(N):
    min_p = 2*(N+1)

    i = 1
    while i*i<=N:
        if N%i==0:
            temp_p = 2*(i+N//i)
            min_p = min(min_p,temp_p)
        i += 1
    return min_p
    pass

print(solution(30))
