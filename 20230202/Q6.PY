#단순한방법
def solutionOne(n):
    answer = -1
    
    for i in range(n):
        if i*i>n:
            break
        elif i*i==n:
            return (i+1)**2
        
    return answer
#근데 이러면 안이뻐서 기각

#이진탐색 접근
def solutionTwo(n):
    num = 2**18
    move = 2**17
    answer = -1
    
    for i in range(19):
        if (num**2)==n:
            answer =  (num+1)**2
        elif (num**2)>n:
            num-=move
        else:
            num+=move
        move = int(move/2)
        
    return answer
#이게 이쁘지~