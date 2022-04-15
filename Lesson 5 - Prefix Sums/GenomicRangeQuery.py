def solution(S, P, Q):
    M = len(P)
    result = [0]*M
    for i in range(M):
        start = P[i]
        end = Q[i]+1
        sequence = S[start:end]
        if "A" in sequence:
            result[i] = 1
        elif "C" in sequence:
            result[i] = 2
        elif "G" in sequence:
            result[i] = 3
        else:
            result[i] = 4
    return result
    pass

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
