def minshrmeasure(arr):
    
    a = arr.copy()
    answer = 1
    smaller = a[0]
    
    for i, ival in enumerate(a):
        if ival < smaller:
            smaller = ival
    
    for i in range(2,smaller+1):
        while (canbediv_arr(a, i)):
            answer = answer*i
            a = div_arr(a, i)
                
    return answer

def canbediv_arr(arr, div):
    for i, ival in enumerate(arr):
        if ival%div != 0:
            return False
    return True

def div_arr(arr, div):
    for i in range(len(arr)):
        arr[i] = arr[i] // div
    
    return arr

def solution(arr):
    answer = 1
    
    LCM = minshrmeasure(arr)
    
    for i, ival in enumerate(arr):
        answer *= ival // LCM
    
    return answer * LCM

arr = [None]*15
arr = [2,6,8,14]
answer = solution(arr)
print(answer)