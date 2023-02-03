def solution(n, s):
    
    maxnum = 0
    answer = []
    startnum = 0
    if(s>9*n):
        startnum = 9**(n-1)*(s-9*n)
    for i in range(startnum, 9**(n-1)*s//n): #1~9까지, 숫자만 따지면 9진수 여러자와 다를 바 없음.
        temparr = []
        temp = i
        check = 0
        for j in range(n):  #모든 경우의 수를(11~99) 브루트포스로 탐색할예정
            check += temp%9 + 1
            temparr.append(temp%9 + 1)
            temp  = temp // 9
        
        tempmax = 1
        if(check != s):
            continue
        else:
            for j in range(n):
                tempmax *= temparr[j]
        
        if tempmax>maxnum:
            answer = temparr.copy()
            maxnum = tempmax
            
    reverse_list(answer)
    
    return answer

def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
        
n = 2
s = 9
answer = solution(n, s)
print(answer)