# implementation of the cyclic rotation algorithm

def solution(A, K):
    rotated_arr = [None] * len(A)
    
    for item in range(len(A)):
        rotated_arr[(item+K) % len(A)] = A[item]
    return rotated_arr

l = [2,7,3,5,10,1,4]
print(f"Array before rotation: {l}")
print(f"Array after rotation: {solution(l,2)}")