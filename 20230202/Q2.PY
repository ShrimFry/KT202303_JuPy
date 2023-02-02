# 시뮬레이션 그대로

N = int(input())
print(f'{N}')
newN = (N%10)*10+int(N/10+N)%10
count = 1
while N != newN:
    newN = (newN%10)*10+int(newN/10+newN)%10
    count+=1


print(count)