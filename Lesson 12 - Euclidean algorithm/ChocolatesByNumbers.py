# Time complexity: O(log(N + M))

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def solution(N, M):
    if N==1:
        return 1
    else:
        return int(N/gcd(N,M)) 
    pass

print(solution(10,4))
