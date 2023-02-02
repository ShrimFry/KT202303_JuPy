string = input('숫자로 이루어진 문자열을 입력하세요. ')
data = int(string)
print(f'숫자로 이루어진 문자열을 입력하세요. {string}')
datat = 0

while data > 0:         #자릿수 역전
    datat *= 10
    datat += data%10
    data = int(data/10)

if string[0]=='0':      #첫글자 0으로 시작하는거에 대해 대처
    datat *=10

data = datat%10
datat = int(datat/10)
print(f'{data} ', end='')

while datat > 0 :
    if((data+(datat%10))>(data*(datat%10))):
        data += datat%10
        print(f'+ {datat%10} ', end='')
    else:
        data *= datat%10
        print(f'x {datat%10} ', end='')
    datat = int(datat/10)
    

print(f'= ', end='')
print(data)