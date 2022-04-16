def solution(A):
    min_slice = (A[0]+A[1])/2
    start_pos = 0
    N = len(A)
    # to find the minimum avarage of slice, we only need to test the slice consists of 2 or 3 elements
    # An excellent explanation of this has been shown in: https://www.youtube.com/watch?v=Xu_hTjFAauk
    # This algorithm is not done by me, which is proposed by this video. The reference link is provided.

    for i in range(N-2):
        avg1 = (A[i]+A[i+1]+A[i+2])/3
        avg2 = (A[i]+A[i+1])/2
        if avg1<min_slice or avg2<min_slice:
            min_slice = min(avg1,avg2)
            start_pos = i
    if min_slice > (A[-1]+A[-2])/2:
        start_pos = N-2
    return start_pos
    pass

print(solution([4,2,2,5,1,5,8]))
