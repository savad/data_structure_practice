
def solution(N, K):
    ans = 0;
    while K:
        if N == 0:
            return -1
        if N >= K: 
            ans += 1
            break
        else:
            ans += 1
            K = K-N
            N = N-1
    return ans

print(solution(4, 10))
