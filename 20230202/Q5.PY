def digitsum(frm, to, num):             #자릿수 a,b 를 입력하면 그 사이의 자연수 합산
    smaller = frm
    larger = to
    if(smaller>to):
        smaller = to
        larger = frm
    
    total = 0
    
    for i in range(smaller, larger):
        digit = int(10**i)
        total += int(num/digit)%10
        
    return total
        
    

n = int(input('숫자를 입력하세요. '))
print(f'숫자를 입력하세요. {n}')

num = n

digit = 0
while num > 0:
    num = int(num/10)
    digit += 1

if(digitsum(0,int(digit/2),n)==digitsum(digit,int(digit/2),n)):
    print("LUCKY")
else:
    print("READY")