

from collections import defaultdict


def solution(N, A, B):
    graph = defaultdict(set)
    for i in range(len(A)):
        graph[A[i]].add(B[i])
        graph[B[i]].add(A[i])
    for i in range(2,N+1):
        if i-1 not in graph[i]:
            return False
    return True
    
print(solution(4, [1, 2, 4, 4, 3], [2, 3, 1, 3, 1]))
