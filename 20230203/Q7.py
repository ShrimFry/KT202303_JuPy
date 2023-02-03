def solution(arr):
    answer = []
    resent = -1
    
    for i, ival in enumerate(arr):
        if(ival != resent):
            answer.append(ival)
            resent = ival
    
    return answer

arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)