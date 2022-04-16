def solution(S):
    N = len(S)
    if N==0:
        return 1
    
    stack = []
    for i in range(N):
        if len(stack)==0 and S[i]==')':
            return 0
        
        if S[i]=='(':
            stack.append(S[i])
        elif S[i]==')' and stack[-1]=='(':
            del stack[-1]
    if len(stack)==0:
        return 1
    else:
        return 0
    pass

print(solution("(()(())())"))
print(solution("())"))
