
def solution(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] != A[j]:
                result = max(result, j - i)
    return result

array = list(range(7500))
print(solution(array))



def solution(A):
    N = len(A)
    result = N-1
    for i in A:
        first = A.pop(0)
        last = A.pop()
        if first == last:
            result -= 1
        else:
            break
    return result

array = list(range(75000))
print(solution(array))
