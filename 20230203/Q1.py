def solution(lottos, win_nums):
    answer = []
    
    cntZ = 0
    cntW = 0
    
    for i, ival in enumerate(lottos):
        if(ival==0):
            cntZ += 1
            continue
        for j, jval in enumerate(win_nums):
            if(ival==jval):
                cntW += 1
                break
    
    answer.append(7-cntZ-cntW)
    answer.append(7-cntW)
    
    if(answer[0]>6):
        answer[0]=6
    if(answer[1]>6):
        answer[1]=6
            
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)