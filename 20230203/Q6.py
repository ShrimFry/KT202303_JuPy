def min_of(a):
    minimum = a[0]
    minind = 0
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum = a[i]
            minind = i
    return minind

def solution(arr):
    answer = []
    minind = min_of(arr)
    
    for i in range(len(arr)):
        if(i == minind):
            continue
        answer.append(arr[i])
    
    return answer

arr = [4, 3, 2, 1]
answer = solution(arr)
print(answer)