from collections import defaultdict

def is_pal(A):
    return A == A[::-1]
    
def remove_char(A):
    hmap = defaultdict(int)
    for i in range(len(A)):
        hmap[A[i]] += 1
    oddCount = 0
    for x in hmap:
        if hmap[x] % 2 != 0:
            oddCount += 1
            oddChar = x

    if (oddCount > 1 or oddCount == 1 and len(A) % 2 == 0):
        A = A.replace(oddChar, "", 1)
        return remove_char(A)
    firstHalf = ""
    secondHalf = ""
    
    for x in sorted(hmap.keys()):
        s = (hmap[x] // 2) * x
        firstHalf = firstHalf + s
        secondHalf = s + secondHalf
    
    if (oddCount == 1):
        return (firstHalf + oddChar + secondHalf)
    else:
        return (firstHalf + secondHalf)

def solution(A):
    
    if is_pal(A):
        return A
    else:
        return remove_char(A)
        
        
            
        
print(solution("abcabghjyfscde"))
