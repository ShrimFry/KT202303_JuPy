def solution(numbers):
    answer = 45
    
    for i, ival in enumerate(numbers):
        answer -= ival
    
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)