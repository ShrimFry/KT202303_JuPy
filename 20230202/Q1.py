# 각 수의 소인수를 이용한 풀이
def solution(a, b):
    answer = 1
    larger = a
    if (b>a):
        larger = b
    
    for i in range(2,larger+1):
        while (a%i==0 or b%i==0):
            answer = answer*i
            if a%i==0:
                a = a/i
            if b%i==0:
                b = b/i
                
    
    return answer

c = solution(a,b)
print(c)

#Q0의 최대공약수를 이용한 풀이
def minshrmeasure(a, b):
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

c = minshrmeasure(a,b)
print(int(a*b/c))