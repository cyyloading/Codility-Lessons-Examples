def solution(A):
  # Hint: implement the procedure of MaxSliceSum twice time, one time is normal order (from 1 to N-1), another time is reversed order (from N-2 to 0)
  N = len(A)
  LS = [0]*N
  RS = [0]*N
  max_sum = 0

  max_L = 0
  temp = 0
  for i in range(1,N-1):
      temp = max(temp+A[i],A[i])
      LS[i] = max(temp,max_L)

  max_R = 0
  temp = 0
  for i in range(N-2, 0, -1):
      temp = max(temp+A[i],A[i])
      RS[i] = max(temp,max_R)

  for i in range(N-2):
      max_sum = max(max_sum, LS[i]+RS[i+2]) # i+1 is the index of Y, used to seperate the double slices.
  return max_sum
  pass

print(solution([3, 2, 6, -1, 4, 5, -1, 2]))
print(solution([3, 2, 6]))
