def solution(X, Y, D):
    result = -1*(-(Y-X)//D)
    return result
    pass

'''
# or
def solution(X, Y, D):
    a = (Y-X)//D
    if (a*D+X >= Y):
        return a
    else:
        return a+1
    pass
'''

print(solution(10, 85, 30))
