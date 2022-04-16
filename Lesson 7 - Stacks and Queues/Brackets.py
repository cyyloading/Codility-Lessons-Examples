def solution(S):
    num = len(S)
    A = []
    if num == 0:
        return 1
    for i in range(0,num):
        if len(A)==0 and (S[i]=="}" or S[i]==")" or S[i]=="]"):
            return 0
        if S[i] == '{':
            A.append(1)
        elif S[i] == '(':
            A.append(2)
        elif S[i] == '[':
            A.append(3)
        elif S[i] == '}' and A[-1]==1:
            del A[-1]
        elif S[i] == ')' and A[-1]==2:
            del A[-1]    
        elif S[i] == ']' and A[-1]==3:
            del A[-1]    
    if len(A)==0:
        return 1
    else:
        return 0
    pass

print(solution("{[()()]}"))
print(solution("([)()]"))
