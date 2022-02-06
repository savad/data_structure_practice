# Write a function def solution(A) that, given an array A consisting of N integers, returns the biggest value of X, which occurs X times. If there is no such value, the function should should return 0


from collections import defaultdict

def solution(A):
    hmap = defaultdict(int)
    for i in range(len(A)):
        hmap[A[i]] += 1
    repeated_x_time = []
    for i in sorted(hmap.keys(), reverse=True):
        if hmap[i] == i:
            return i
    return 0
    
    
        
        
            
        
print(solution([2, 4, 5, 5, 6, 2, 3, 3,3,3,5,5,5]))
