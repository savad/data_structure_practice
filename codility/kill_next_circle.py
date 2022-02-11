import json

def solution(n):
    a = [i for i in range(1, n+1)]
    while len(a)>1:
        if len(a) % 2 == 1:
            a=a[::2]
            a=a[1:]
        else:
            a=a[::2]
    return a[::2][0]

a = solution(1000)    
print(a)



