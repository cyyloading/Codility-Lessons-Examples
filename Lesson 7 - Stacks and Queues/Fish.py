def solution(A, B):
    num = 0
    N = len(B)
    stack = []
    for i in range(N):
        if B[i]==1:
            stack.append(A[i])
        else:
            while len(stack)>0:
                if stack[-1]<B[i]:
                    del stack[-1]
                else:
                    break
            if len(stack)==0:
                num += 1
    num += len(stack)
    return num
    pass

  print(solution([4,3,2,1,5],[0,1,0,0,0]))
