def measurenum(num):        #약수 개수 리턴 함수
    measurecnt = 0
    for i in range(1,num+1):
        if(num%i==0):
            measurecnt += 1
    return measurecnt

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        msrcnt = measurenum(i)
        if(msrcnt%2):
            answer-=i
        else:
            answer+=i
    
    return answer

left = 13
right = 17
c = solution(left, right)
print(c)