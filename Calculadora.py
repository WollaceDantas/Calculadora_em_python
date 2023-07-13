#calculadora em python
while True:
    x= input('Digite o primeiro número:')
    y= input('Digite o segundo número:')
    z= input('Digite a operação:')

    x=int(x)
    y=int(y)

    if z=='+':
        print(f'O resultado de {x}+{y} é igual a', x+y,'.')
        
    elif z=='-':
        print(f'O resultado de {x}-{y} é igual a',x-y)

    elif z=='*':
        print(f'O resultado de {x}*{y} é igual a', x*y)

    elif z=='/':
        print(f'O resultado de {x}/{y} é igual a', x/y)

    else:
        print(f'Você precisa digitar uma das 4 operações.')
        