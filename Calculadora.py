#calculadora em python
while True:
    x= int(input('Digite o primeiro número:'))
    y= int(input('Digite o segundo número:'))
    z= input('Digite a operação:')

    if z=='+':
        print('O resultado de x+y é igual a', x+y,'.')
        
    elif z=='-':
        print('O resultado de x-y é igual a',x-y)

    elif z=='*':
        print('O resultado de x*y é igual a', x*y)

    elif z=='/':
        print('O resultado de x/y é igual a', x/y)

    else:
        print('Você precisa digitar uma das 4 operações.')
        