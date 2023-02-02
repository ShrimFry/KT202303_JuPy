# 각 수의 소인수 분해 및 공통 인수만 곱

def solution(a, b):
    answer = 1
    smaller = a
    if (b>a):
        smaller = b
    
    for i in range(2,smaller+1):
        while (a%i==0 and b%i==0):
            answer = answer*i
            a = a/i
            b = b/i
                
    
    return answer

c = solution(a,b)
print(c)